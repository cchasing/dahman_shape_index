import numpy as np

def cal_slip_size(sframe, eframe, pos):
    Sz_slip = [] # slip size
    Dur = []     # slip duration
    for i in range(len(sframe)):
        Sz_slip.append(pos[eframe[i]]-pos[sframe[i]])
        Dur.append(eframe[i]-sframe[i])
    return Sz_slip, Dur

def cal_force_drop(sframe, eframe, fspring):
    fdrop = [] # drop in spring force  = start force -  end force
    for i in range(len(sframe)):
        fdrop.append(fspring[sframe[i]]-fspring[eframe[i]])
    return fdrop

def moving_average(a, n=4):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n-1:]/n

def max_drop_rate(sframe, eframe, Y):
    max_rate = []
    for i in range(len(sframe)):
        x = np.linspace(sframe[i],eframe[i],eframe[i]-sframe[i]+1)
        y = Y[sframe[i]:eframe[i]+1]
        if len(y)>10:
            movy = moving_average(y)
            #The gradient is computed using second order accurate central differences
            #in the interior points and either first or second order accurate one-sides
            #(forward or backwards) differences at the boundaries.
            #The returned gradient hence has the same shape as the input array.
            dydx = np.gradient(movy)
            max_rate.append(max(abs(dydx)))
        else:
            dydx = np.gradient(y)
            max_rate.append(max(abs(dydx)))
    return max_rate

def shape_index(max_rate, slip_size): # y=force, xstart, xend=list of start time, end time
    shape_ind = np.sqrt(slip_size)/np.array(max_rate)
    return shape_ind
