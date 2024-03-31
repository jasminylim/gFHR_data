# File: interpolate_data.py
# Author: Jasmin Lim
# Descritpion: interpolate SAM data for constant time step
# Date Created: March 12, 2024
# Edits

import numpy as np
import matplotlib.pyplot as plt

# read data from file
filename = "gFHR-LF-10.csv"

with open("SAM/"+filename, "r") as file:
    names = file.readline()
    names = names.strip().split(",")
    
data = np.genfromtxt("SAM/"+filename, dtype="float", delimiter=",", skip_header=1)

print(data.shape)

# interpolate data for a 5[s] time step
ti = np.arange(data[0,0],data[-1,0],5)
xi = np.zeros((ti.shape[0],data.shape[1]))
for i in range(data.shape[1]):
    xi[:,i] = np.interp(ti, data[:,0], data[:,i])

print(xi.shape)

# write data to file
header = ",".join(names)
np.savetxt("SAM_interp/"+filename, xi, delimiter=",", header=header, comments='')

