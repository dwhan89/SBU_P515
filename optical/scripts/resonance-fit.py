import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import oppumpmagres_funcs as func

# for converting V --> frequency (Hz)
mid_freq = 200e3
step_freq = 50
num_freq = 1000

# for data handling
datafile = "../data/rb85res_run3.txt"
I_data = []
f_data = []
maxI = -99999;

# get photodiode voltage (proportional to transmitted intensity)
# vs. temperature data from file and calculate voltage vs.
# number density from it
with open(datafile,newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
     # if row[1] and row[2] exist...?
          I = float(row[1])
          if I > maxI: maxI = I
          V = float(row[0])
          f = func.VtoFreq(V,mid_freq,step_freq,num_freq)
          I_data.append(I)
          f_data.append(f)

# Normalize intensity
Inorm_data = [x / maxI for x in I_data]

#fit the data
#popt, pcov = curve_fit(gauss_function,f_data,Inorm_data,p0=[0.02,5,2])
popt, pcov = curve_fit(func.lorentzian_function,f_data,Inorm_data,p0=[0.02,mid_freq,10e3])
perr = np.sqrt(np.diag(pcov))
x = np.linspace(min(f_data),max(f_data), num=1000)

# plot I/I_0 vs. n 
plt.scatter(f_data,Inorm_data,label='data')
plt.plot(x,func.lorentzian_function(x,*popt),'r-',label='Lorentzian fit')
plt.legend()
plt.ylabel("$I/I_{0}$")
plt.xlabel("frequency (Hz)")

print("mean = %f " % popt[1])
print("sigma(mean) = %f " % perr[1])

plt.show()
