import numpy as np
import matplotlib.pyplot as plt
from power_law_fitting import power_fit

def plot_log_pdf(x, Nbin = 20):
    plt.figure()
    bins = np.logspace(np.log10(np.min(x)),
                       np.log10(np.max(x)),
                       num = Nbin)
    hist, bin_edges = np.histogram(x, bins = bins, density = True, ) # bin it into n = N//10 bins
    bin_edges = bin_edges[:-1] + (bin_edges[1] - bin_edges[0])/2   # convert bin edges to centers
    plt.scatter(bin_edges, hist)
    plt.xscale('log')
    plt.yscale('log')
    sort_hist = sorted(hist)  # for automatically setting the ylim following
    plt.xlim([np.min(x)/2.0, np.max(x)*2.0])
    plt.ylim([np.average(sort_hist[0:4])/2.0, np.max(hist)*2.0])
    plt.xlabel('s, slip size')
    plt.ylabel('pdf(s)')
    plt.title('pdf')
    # a0,a1 = power_fit(bin_edges, hist)
    # plt.plot(bin_edges, a0*np.array(hist)**a1)
    plt.show()
    return bin_edges, hist

def loglog_plot(x, y, xytitle):
    plt.figure()
    plt.scatter(x, y)
    plt.xlim([np.min(x)/2, np.max(x)*2])
    plt.ylim([np.min(y)/2, np.max(y)*2])
    plt.yscale('log')
    plt.xscale('log')
    plt.title(xytitle)
    plt.show()
