import numpy as np

def mov_mean(x, window = 10):
    return None

def identify_slips(vels, vel_thd):
    sframe = []
    eframe = []
    i = 1
    ended = True  # True if a slip ended and need to look for a start
    while i < len(vels):
        if ended:
            if vels[i-1] < vel_thd and vels[i] > vel_thd:
                sframe.append(i-1)
                ended = False
        else:
            if vels[i-1] > vel_thd and vels[i] < vel_thd:
                eframe.append(i)
                ended = True
        i += 1
    if len(eframe) < len(sframe): # drop off the last slip event start frame which is without the end frame
        sframe.pop()
    return sframe, eframe
