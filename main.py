#Huge thanks to: https://stackoverflow.com/users/1034747/ryan-martin
#for providing this answer: https://stackoverflow.com/a/40157297

import sounddevice as sd
import numpy as np
from playsound import playsound

#These variables are used so that small spikes won't trigger the sound
#I don't know if 7 ticks is the perfect value, so you can change it if you want to
spiked = False
counter = 7
spike_max = 15

def print_sound(indata, outdata, frames, time, status):
    global counter, spiked
    volume_norm = np.linalg.norm(indata)*10
    print (int(volume_norm))
    counter-=1
    if not spiked:
        counter = 7
    if int(volume_norm) > spike_max:
        spiked = True
        counter-=1
    else:
        spiked = False
    if counter<=0:
        playsound('beep.mp3')

with sd.Stream(callback=print_sound):
    sd.sleep(12 * 3600 * 1000)