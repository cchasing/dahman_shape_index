import pandas as pd
import numpy as np

# for
def read_wall_info(dirInput):
    df_wallinfo = pd.read_csv(dirInput, header = None, sep='\s+')
    df_wallinfo.columns = ["Frame","Xperiodic", "YPosition","XVelocity",
    "YVelocity","XPosition","TopForceX","TopForceY","BottomForceX", "BottomForceY",
    "Springforce"]
    return [df_wallinfo["Frame"].values.tolist(),df_wallinfo["XPosition"].values.tolist(),
    df_wallinfo["Springforce"].values.tolist(),df_wallinfo["XVelocity"].values.tolist()]
