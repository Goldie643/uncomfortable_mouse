from pynput import mouse
from playsound import playsound
import time
import math
import matplotlib.pyplot as plt
import numpy as np


def dr(r1,r2):
    dx = r1[0]-r2[0]
    dy = r1[1]-r2[1]
    return math.sqrt(dx**2+dy**2)

def on_click(x, y, button, pressed):
    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))
    # if not pressed:
    #     # Stop listener
    #     return False
    pass

def on_scroll(x, y, dx, dy):
    # print('Scrolled {0} at {1}'.format(
    #     'down' if dy < 0 else 'up',
    #     (x, y)))
    pass

# listener = mouse.Listener(
#     on_move=on_move,
#     on_click=on_click,
#     on_scroll=on_scroll)
# listener.start()

sounds_dir = "sounds/"

max_speed = 50 # px/update
max_accel = 20 # px/update
accel_thresh = 0.7*max_accel

# Store the last three vertices
# For speed and accel
positions = [(0,0),(0,0)]
# The longer this array, the more averaged the accel is
speeds = [0,0]

n_files = 10

speed_bin_size = max_speed/n_files
accel_bin_size = max_accel/n_files

bars = []
n_bars = 10
for i in range(n_bars):
    bar = ""
    for j in range(n_files):
        if(j != i):
            bar+="-"
        else:
            bar+="X"
    bars.append(bar)

global_counter = 0
update_interval = 3

mouse = mouse.Controller()

woah_spacing = 1 # min. time between woahs
last_woah = -9999

while True:
    global_counter+=1
    (x,y) = mouse.position
    positions.pop(0)
    positions.append((x,y))

    distance_moved = dr(positions[-1],positions[-2])
    if(distance_moved!=0):
        speeds.pop(0)
        speeds.append(distance_moved)

        accel = (speeds[-1]-speeds[-2])
        if(accel>accel_thresh and (time.time()-last_woah) > woah_spacing):
            playsound(sounds_dir+"woah.wav")
            last_woah = time.time()
        # for i in range(n_files):
        #     if(speeds[-1] > i*speed_bin_size and speeds[-1] < (i+1)*speed_bin_size):
        #         # print("%02i\r"%(i+1),end="")
        #         for j in range(n_files):
        #             if(accel > j*accel_bin_size and accel < (j+1)*accel_bin_size):
        #                 print("Speed: "+bars[i]+"   Accel: "+bars[j]+"\r",end="")
        #         # playsound(sounds_dir+"%02i.wav"%(i+1),block=True)
        #         if(global_counter%update_interval==0):
        #             # playsound(sounds_dir+"%02i.wav"%(i+1),block=False)
        #             global_counter=0
        #         break
    continue