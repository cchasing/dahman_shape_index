import numpy as np

def skewly(XX, sframe, eframe):
    ### return the deviation of the index of the max value of XX away from the center of the XX window
    ### which normalized by the duration of the window
    sky = []
    for i in range(len(eframe)):
        stt = sframe[i]
        end = eframe[i]
        dur = end - stt
        x_win = XX[stt:end+1]
        max_ind = np.argmax(x_win)
        sky.append(abs(max_ind-dur/2)/dur)
    return sky
