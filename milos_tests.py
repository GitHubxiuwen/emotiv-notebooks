# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from emotiv import epoc, utils, analysis
from IPython.display import clear_output, display
import pandas, tables
import time

# <codecell>

def normalize(column):
    return (column - column.mean())/(column.max() - column.min())

# <codecell>

column = df.O2.name
normalize(df[column]).plot()
normalize(df[column + '_QUAL']).plot(c='r')

# <codecell>

normalize(fdf.gyroX).plot()
normalize(fdf.gyroY).plot(c='r')

# <codecell>

CHANNELS = ("F3", "FC5", "AF3", "F7", "T7", "P7", "O1", "O2", "P8",  "T8",  "F8", "AF4", "FC6", "F4")
CHANNEL_X = (156, 120, 133, 97, 74, 101, 145, 258, 300,  333,  305, 269, 277, 247)
CHANNEL_Y = (112, 167, 75, 133, 207, 301, 342, 342, 301,  207,  133, 75, 167, 112)

# <codecell>

red_to_green = get_cmap(name='RdYlGn')
bg = imread('emotivCMSDRL.png')
imshow(bg)
scatter(CHANNEL_X, CHANNEL_Y, c=[df.tail(1)[c + '_QUAL'].sum() for c in CHANNELS], s=150, cmap=red_to_green);

# <codecell>

red_to_green = get_cmap(name='RdYlGn')
bg = imread('emotivCMSDRL.png')
f, ax = subplots()
imshow(bg)
row = df.tail(1)
for i, row in df.iterrows():
    if i % 1000 != 0: continue
    scatter(CHANNEL_X, CHANNEL_Y, c=[row[c + '_QUAL'].sum() for c in CHANNELS], s=150, cmap=red_to_green)
    clear_output()
    display(f)

# <codecell>

df.groupby(by='packets_skipped').packets_skipped.count()

# <codecell>

from tempfile import NamedTemporaryFile

VIDEO_TAG = """<video controls>
 <source src="data:video/x-m4v;base64,{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>"""

def anim_to_html(anim):
    if not hasattr(anim, '_encoded_video'):
        with NamedTemporaryFile(suffix='.mp4') as f:
            anim.save(f.name, fps=20, extra_args=['-vcodec', 'libx264'])
            video = open(f.name, "rb").read()
        anim._encoded_video = video.encode("base64")
    
    return VIDEO_TAG.format(anim._encoded_video)

from IPython.display import HTML

def display_animation(anim):
    plt.close(anim._fig)
    return HTML(anim_to_html(anim))

# <codecell>

from matplotlib import animation

fig = figure(figsize=(15,5))
ax = axes(xlim=(0,2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)

# call our new function to display the animation
display_animation(anim)

# <codecell>

import tables, time, libeeg
from IPython.display import display, clear_output

# <codecell>

len(libeeg.CHANNELS)

# <codecell>

def test(rec):
    SAMPLING_RATE = 128
    show_rows = SAMPLING_RATE * 5
    f = figure(figsize=(15,5))
    try:
        while True:
            h5 = tables.open_file(rec.file_name)
            tbl = h5.root.eeg.signal
            rows = tbl[-show_rows:]
            h5.close()
            tick_times = [row['tick_time'] for row in rows]
            signals, qualities = {}, {}
            for channel in libeeg.CHANNELS:
                signals[channel] = [row[sensor] for row in rows]
                qualities[channel] = [row[sensor + '_QUAL'] for row in rows]
            
            for i, channel in enumerate(libeeg.CHANNELS):
                subplot(2, 7, i+1)
                plot(tick_times, signals[channel], color='b')
                xlim(tick_times[0], tick_times[-1])            
            clear_output()
            display(f)
            time.sleep(1./SAMPLING_RATE*2)
    except KeyboardInterrupt:
        pass

# <codecell>

rec.stop()

# <codecell>

rec.stop()

# <codecell>

rec.is_recording()

# <codecell>

def load_rows(file_name):
    h5 = tables.open_file(file_name)
    tbl = h5.root.eeg.signal
    #rows = tbl[-show_rows:]
    rows = tbl[:]
    h5.close()
    return rows

# <codecell>

rows = load_rows('recordings/test_recording.h5')

# <codecell>

rows[0]['tick_time']

# <codecell>

frows = [row for row in rows if row['state'] == 'blinking']

# <codecell>

def plot_all_channels(rows):
    tick_times = [row['tick_time'] for row in rows]
    signals, qualities = {}, {}
    for channel in libeeg.CHANNELS:
        signals[channel] = [row[channel] for row in rows]
        qualities[channel] = [row[channel + '_QUAL'] for row in rows]
    
    f = figure(figsize=(15,5))
    for i, channel in enumerate(libeeg.CHANNELS):
        subplot(2, 7, i+1)
        plot(tick_times, signals[channel], color='b')
        xlim(tick_times[0], tick_times[-1])
    display(f)

# <codecell>

import pandas

# <codecell>

df = pandas.read_hdf('recordings/test_recording.h5', '/eeg/signal')
df.set_index(keys='tick_time', verify_integrity=True, inplace=True)

# <codecell>

len(df)

# <codecell>

figure(figsize=(20,7))

fstate = pandas.factorize(df.state)
df['fstate'] = fstate[0]

subplot(3,1,1)
for i, channel in enumerate(libeeg.CHANNELS):
    df.fstate.plot()
    yticks(arange(len(fstate[1])), fstate[1])
subplot(3,1,2)
for i, channel in enumerate(libeeg.CHANNELS):
    df[channel].plot()
subplot(3,1,3)
for i, channel in enumerate(libeeg.CHANNELS):
    df[channel + '_QUAL'].plot()
xlim

# <codecell>

def data_range(arr):
    return min(arr), max(arr)

# <codecell>

df.columns

# <codecell>

for c in df.columns:
    if not '_QUAL' in c:
        continue
    print max(df[c])

# <codecell>

plot_all_channels(rows)

# <codecell>

import emotiv

# <codecell>

emotiv.epoc??

# <codecell>

from itertools import chain
for i, x in enumerate(sorted(chain(*emotiv.epoc.EPOC.bit_indexes.values()))):
    print i, x

# <codecell>

df = pandas.read_hdf('recordings/test_recording.h5', '/eeg/signal')
#df['tick_time_dt64'] = (df.tick_time/1000000.0).map(datetime.datetime.utcfromtimestamp).map(np.datetime64)
df['tick_time_dt64'] = df.tick_time
df.set_index(keys='tick_time_dt64', verify_integrity=True, inplace=True, drop=False)

# <codecell>

def plot_channels(df, state=None, normalizer=lambda x: x):
    figure(figsize=(20,7))
    
    if state:
        df = df[df.state==state]

    fstate = pandas.factorize(df.state)
    df['fstate'] = fstate[0]
    
    subplot(3,1,1)
    for i, channel in enumerate(libeeg.CHANNELS):
        df.fstate.plot()
        yticks(arange(len(fstate[1])), fstate[1])
    xlim(df.tick_time_dt64.min(), df.tick_time_dt64.max())
    
    subplot(3,1,2)
    for i, channel in enumerate(libeeg.CHANNELS):
        normalizer(df[channel]).plot()
    xlim(df.tick_time_dt64.min(), df.tick_time_dt64.max())
    
    subplot(3,1,3)
    for i, channel in enumerate(libeeg.CHANNELS):
        df[channel + '_QUAL'].plot()
    xlim(df.tick_time_dt64.min(), df.tick_time_dt64.max())

# <codecell>

def normalize(column):
    return (column - column.mean())/(column.max() - column.min())

# <codecell>

def remove_mean(column):
    return column - column.mean()

# <codecell>

df.state.unique()

# <codecell>

#plot_channels(df, state='blinking')
#plot_channels(df)
fdf=df
fdf = df[df.state=='eyes_left']
plot_channels(df[df.tick_time.between(fdf.tick_time.min() - 5*10**6 , fdf.tick_time.max() + 5*10**6)])

# <codecell>


