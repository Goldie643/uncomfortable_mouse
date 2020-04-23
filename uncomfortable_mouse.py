from pynput import mouse
from playsound import playsound
import time
import math
import matplotlib.pyplot as plt
import numpy as np

sounds_dir = "sounds/sine/"

max_speed = 100 # px/s

# Store the last three vertices
# For speed and acceleration
positions = [(0,0),(0,0),(0,0)]
speeds = [0,0,0] 
times = [0,0,0]

all_speeds = []

n_files = 10

bin_size = max_speed/n_files

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

def dr(r1,r2):
    dx = r1[0]-r2[0]
    dy = r1[1]-r2[1]
    return math.sqrt(dx**2+dy**2)

def on_move(x, y):
    global global_counter
    global_counter+=1
    positions.pop(0)
    positions.append((x,y))

    times.pop(0)
    times.append(time.time())

    distance_moved = dr(positions[-1],positions[-2])
    dt = times[-1]-times[-2]
    speeds.pop(0)
    # speeds.append(distance_moved/dt)
    speeds.append(distance_moved)
    all_speeds.append(speeds[-1])

    acceleration = (speeds[-1]-speeds[-2])/dt
    for i in range(n_files):
        if(speeds[-1] > i*bin_size and speeds[-1] < (i+1)*bin_size):
            # print("%02i\r"%(i+1),end="")
            print(bars[i]+"\r",end="")
            # playsound(sounds_dir+"%02i.wav"%(i+1),block=True)
            if(global_counter%update_interval==0):
                playsound(sounds_dir+"%02i.wav"%(i+1),block=False)
                global_counter=0
            break


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

listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

while True:
    continue
