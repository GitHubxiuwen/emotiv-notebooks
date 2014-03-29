# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import libeeg

# <codecell>

rec = libeeg.EEGRecorder('recordings/youtube.h5')

# <codecell>

rec.start()

# <codecell>

rec.is_recording()

# <codecell>

rec.tag('smile')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('blinking')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('eyes_left')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('eyes_right')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('eyes_closed')

# <codecell>

rec.tag('eyes_open')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('eyes_up')

# <codecell>

rec.tag('eyes_down')

# <codecell>

rec.neutral()

# <codecell>

rec.stop()

# <codecell>

rec.tag('head_left')

# <codecell>

rec.tag('head_right')

# <codecell>

rec.tag('head_up')

# <codecell>

rec.tag('head_down')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('brows_up')

# <codecell>

rec.neutral()

# <codecell>

rec.tag('frown')

# <codecell>

rec.stop()

# <codecell>

rec.is_recording()

# <codecell>

rec.tag('song')

# <codecell>

rec.tag('song_eyes_closed')

# <codecell>

rec.neutral()

# <codecell>

rec.stop()

# <codecell>


