import numpy as np
from scipy import optimize

def power_fit(xdata, ydata):
    logx = np.log10(xdata)
    logy = np.log10(ydata)
    fitfunc = lambda p, x: p[0]+p[1]*x
    errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
    #out = optimize.leastsq(errfunc, pinit, args=(logx, logy, logyerr), full_output=1)
    # pfinal = out[0]
    # covar = out[1]
    # print(pfinal,covar)
    # return pfinal, covar
