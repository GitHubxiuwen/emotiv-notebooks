# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from emotiv import epoc
import multiprocessing as mp
import tables, time
from path import path
import pandas
from IPython.display import clear_output, display
from matplotlib.pylab import *
from lockfile import FileLock

# <codecell>

class EEGTick(tables.IsDescription):
    state = tables.StringCol(16)
    packet = tables.UInt64Col()
    tick = tables.UInt8Col()
    tick_time = tables.UInt64Col()
    packets_skipped = tables.UInt8Col()
    battery = tables.UInt8Col()
    gyroX = tables.UInt16Col()
    gyroY = tables.UInt16Col()
    F3 = tables.Float32Col()
    FC5 = tables.Float32Col()
    AF3 = tables.Float32Col()
    F7 = tables.Float32Col()
    T7 = tables.Float32Col()
    P7 = tables.Float32Col()
    O1 = tables.Float32Col()
    O2 = tables.Float32Col()
    P8 = tables.Float32Col()
    T8 = tables.Float32Col()
    F8 = tables.Float32Col()
    AF4 = tables.Float32Col()
    FC6 = tables.Float32Col()
    F4 = tables.Float32Col()
    F3_QUAL = tables.Float32Col()
    FC5_QUAL = tables.Float32Col()
    AF3_QUAL = tables.Float32Col()
    F7_QUAL = tables.Float32Col()
    T7_QUAL = tables.Float32Col()
    P7_QUAL = tables.Float32Col()
    O1_QUAL = tables.Float32Col()
    O2_QUAL = tables.Float32Col()
    P8_QUAL = tables.Float32Col()
    T8_QUAL = tables.Float32Col()
    F8_QUAL = tables.Float32Col()
    AF4_QUAL = tables.Float32Col()
    FC6_QUAL = tables.Float32Col()
    F4_QUAL = tables.Float32Col()

# <codecell>

CHANNELS = ("F3", "FC5", "AF3", "F7", "T7", "P7", "O1", "O2", "P8",  "T8",  "F8", "AF4", "FC6", "F4")
SAMPLING_RATE = 128

# <codecell>

def data_collector(state_queue, file_name, dummy):
    import tables, time, numpy
    from matplotlib.dates import date2num
    from emotiv import epoc
    from path import path
    from itertools import izip
    from datetime import datetime
    from lockfile import FileLock
    
#    lock = FileLock(file_name)
    if path(file_name).exists():
        raise Exception('Recording "{}" already exists'.format(file_name))
#         h5file = tables.open_file(file_name, mode="a", title='[Title] EEG Signal')
#         h5table = h5file.root.eeg.signal
    else:
        h5file = tables.open_file(file_name, mode="w", title='[Title] EEG Signal')
        h5group = h5file.create_group("/", 'eeg', '[Group] EEG signal')
        h5table = h5file.create_table(h5group, 'signal', EEGTick, "[Table] EEG Signal")
    row = h5table.row
    
    e = epoc.EPOC(method='dummy' if dummy else 'libusb')
    try:
        cycle, last_tick, last_packet = -1, -1, 0
        current_state = 'neutral'
        while True:
            if dummy:
                time.sleep(0.0077)
            sample, tick, tick_time = e.get_sample(), e.counter, numpy.datetime64(datetime.utcnow()).astype(numpy.uint64)
            if not state_queue.empty():
                current_state = state_queue.get_nowait()
            if current_state == 'quit':
                break
            if tick < last_tick and last_tick != -1:
                cycle += 1
            last_tick = tick
            packet = cycle * (SAMPLING_RATE + 1) + tick
            packets_skipped = packet - last_packet - 1
            last_packet = packet
            if tick == 128 or cycle==-1:
                continue
#             with lock:
            row['state'], row['packet'], row['tick'], row['tick_time'] = current_state, packet, tick, tick_time
            row['packets_skipped'], row['battery'] = packets_skipped, e.battery
            row['gyroX'], row['gyroY'] = e.gyroX, e.gyroY
            for channel, value in izip(CHANNELS, sample):
                row[channel], row[channel + '_QUAL'] = value, e.quality[channel]
            row.append()
            h5table.flush()
    except KeyboardInterrupt:
        pass
    finally:
        e.disconnect()
#         with lock:
        h5table.flush()

# <codecell>

class EEGRecorder(object):
    def __init__(self, file_name='recordings/recording.h5', dummy=False, overwrite=False):
        self.dummy = dummy
        self.file_name = file_name
        if overwrite and path(file_name).exists():
            path(file_name).remove()
        self._setup_process()

    def _setup_process(self):
        self.__state_queue = mp.Queue(maxsize=5)
        self.__collector = mp.Process(name='block', target=data_collector,
                                      args=(self.__state_queue, self.file_name, self.dummy))
        self.__collector.daemon = True
        
    def start(self):
        if self.is_recording():
            return
        self.__collector.start()
    
    def stop(self):
        if not self.is_recording():
            return
        self.__state_queue.put('quit')
        self.__collector.join()
        self._setup_process()

    def is_recording(self):
        return self.__collector.is_alive()
    
    def tag(self, tag=None):
        self.__state_queue.put(tag or 'neutral')
    
    def neutral(self):
        self.tag()
    
    def get_df(self):
        return pandas.read_hdf(self.file_name, '/eeg/signal')
    
    def sensor_monitor(self, sensor, duration=5):
        
        show_rows = SAMPLING_RATE * duration
#         lock = FileLock(self.file_name)
        f = figure(figsize=(15,5))
        try:
            while True:
#                 with lock:
                h5 = tables.open_file(self.file_name)
                tbl = h5.root.eeg.signal
                rows = tbl[-show_rows:]
                h5.close()
                tick_times = [row['tick_time'] for row in rows]
                signals = [row[sensor] for row in rows]
#                 qualities = [row[sensor + '_QUAL'] for row in rows]
                plot(tick_times, signals, color='b')
                xlim(tick_times[0], tick_times[-1])
                clear_output()
                display(f)
                time.sleep(1./SAMPLING_RATE*2)
        except KeyboardInterrupt:
            pass

