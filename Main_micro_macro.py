import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
from pathlib import Path
from read_wall_info import read_wall_info
from identify_slips import identify_slips
from slip_measure import cal_slip_size, cal_force_drop, shape_index, max_drop_rate
from plot_pdfs import plot_log_pdf, loglog_plot
from skewness import skewly


home = str(Path.home())
wallinfo_dir = home + "/Dropbox/2D_Stik_Slip/2D_slip_distribution_analysis/wall_infos/"
data_folder = "/Dropbox/2D_Stik_Slip/2D_slip_distribution_analysis/dahman_shape_index/data/"
long_run_file = "wallinfo_reference_10th.dat"
vel_threshold = 2e-3
[time, xpos, fspring, xvel] = read_wall_info(wallinfo_dir + long_run_file)
starts, ends = identify_slips(xvel, vel_threshold) #find the start, end frame of slip events
slip_size, duration = cal_slip_size(starts, ends, xpos)
force_drop = cal_force_drop(starts, ends, fspring)
bC = np.array(pd.read_csv(home+data_folder+"broken_contacts_1_299999_10th.dat",sep ='\s+', skiprows = 1,))
ftfns = np.array(pd.read_csv(home+data_folder+"ftfn_ratios.dat",sep ='\s+', skiprows = 1,))
bC_force = bC[:,2]
bC_number = bC[:,1]
ftfn_ratio = ftfns[:,1]
max_drate = max_drop_rate(starts, ends, ftfn_ratio)
shape_ind = shape_index(max_drate, slip_size)
centralness = skewly(bC_number,starts, ends)

plt.scatter(slip_size,centralness)
plt.xlabel('slip size')
plt.ylabel('skewness')
plt.xscale('log')
plt.show()

bin_mid, hist = plot_log_pdf(slip_size, 50)
loglog_plot(slip_size, duration, 'duration')
loglog_plot(slip_size, max_drate, 'max ftfn_ratio rate')
loglog_plot(slip_size, shape_ind, 'shape index' )
# power_fit(bin_mid, hist)
