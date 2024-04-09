# file: plot.py
# description: plot SAM gFHR data
# author: Jasmin Lim
# date created: April 4, 2024

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filename = "SAM/gFHR-LF-11.csv"

    col_names = ["time",
             "target_power",
             "core_energy"]
    data = pd.read_csv(filename, sep=',', header=0, usecols=col_names)[col_names].to_numpy()

    fig, ax = plt.subplots(1,2,figsize=(15,4))
    for i in range(1,len(col_names)):
        ax[i-1].plot(data[:,0]/3600, data[:,i])
        ax[i-1].set_xlabel(r"Time [hr]")
        ax[i-1].set_ylabel(r"{}".format(col_names[i]))
    fig.suptitle(r"{}".format(filename))
    plt.savefig("plot_data.png", dpi=350)

