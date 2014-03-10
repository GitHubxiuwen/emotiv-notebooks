# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import libeeg

# <codecell>

recorder = libeeg.EEGRecorder(overwrite=True)

# <codecell>

recorder.start()

# <codecell>

recorder.is_recording()

# <codecell>

recorder.tag('blinking')

# <codecell>

recorder.neutral()

# <codecell>

# stop monitoring with a kernel interrupt (CTRL+M I)
recorder.sensor_monitor('F3')

# <codecell>

recorder.stop()

# <codecell>

df = recorder.get_df()

# <codecell>

', '.join(reversed(df.columns))

# <codecell>

dfi = df.reindex(index=df.tick_time, method='ffill')

# <codecell>

df.packets_skipped.plot()
df.packet.plot()
df.tick.plot()

# <codecell>

def normalize(column):
    column_range = column.max() - column.min()
    return (column - column.mean())/(column_range or 1)

