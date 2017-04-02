import math
import numpy as np
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

#marker size
ms = 5.0

datafile2 = "../data/eff/S2-eff.txt"
eff2_list = []
HV2_list  = []
datafile3 = "../data/eff/S3-eff.txt"
eff3_list = []
HV3_list  = []

# S3: std(x=2.4) = 0.6210
eff3_err  = 0.6210 
# S2: std(x=2.4) = 0.3726
# S2: std(x=2.0) = 2.5935
eff2_err  = (0.372633 + 2.5934)/ 2.0 

with open(datafile2,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              eff2 = float(row[0])
              HV2  = abs(float(row[1]))
              eff2_list.append(eff2)
              HV2_list.append(HV2)

with open(datafile3,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              eff3 = float(row[0])
              HV3  = abs(float(row[1]))
              eff3_list.append(eff3)
              HV3_list.append(HV3)

eff2_err_list = np.full((len(eff2_list),), eff2_err) * 2
eff3_err_list = np.full((len(eff3_list),), eff3_err) * 2

# add a vertical line at x = 2.4k
plt.axvline(x=2.4, color='k', linestyle='--', label='HV = 2.4kV')

plt.xlabel('High Voltage [kV]',size=22,fontweight='bold')
plt.ylabel('Efficiency [%]',size=22,fontweight='bold')
plt.grid(True, which='both')
plt.errorbar(HV2_list,eff2_list, yerr=eff2_err_list ,color='red',label='S2 efficiency', ms=ms, ecolor='k', fmt='o')
plt.errorbar(HV3_list,eff3_list, yerr=eff3_err_list, color='blue',label='S3 efficiency', ms=ms, ecolor='k', fmt='o')
plt.legend(loc=2)

plt.show(block=True)

