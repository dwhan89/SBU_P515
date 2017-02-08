import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# for converting V --> frequency (Hz)
mid_freq = 200e3
step_freq = 50
num_freq = 1000

def VtoFreq(V):
    return (V/10)*(num_freq*step_freq)+mid_freq-step_freq*(num_freq/2)

def gauss_function(x,a,x0,sigma):
    return 1 - a*np.exp(-(x-x0)**2/(2*sigma**2))

def lorentzian_function(x,a,x0,sigma):
    return 1 - a*(0.5*sigma)/((x-x0)**2+0.25*(sigma)**2)

I_data = []
f_data = []
maxI = -99999;

# get photodiode voltage (proportional to transmitted intensity)
# vs. temperature data from file and calculate voltage vs.
# number density from it
with open("../data/rb85res_run3.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
     # if row[1] and row[2] exist...?
          I = float(row[1])
          if I > maxI: maxI = I
          V = float(row[0])
          f = VtoFreq(V)
          I_data.append(I)
          f_data.append(f)

# Normalize intensity
Inorm_data = [x / maxI for x in I_data]

#fit the data
#popt, pcov = curve_fit(gauss_function,f_data,Inorm_data,p0=[0.02,5,2])
popt, pcov = curve_fit(lorentzian_function,f_data,Inorm_data,p0=[0.02,200e3,10e3])
perr = np.sqrt(np.diag(pcov))
x = np.linspace(min(f_data),max(f_data), num=1000)

# plot I/I_0 vs. n 
plt.scatter(f_data,Inorm_data,label='data')
plt.plot(x,lorentzian_function(x,*popt),'r-',label='Lorentzian fit')
plt.legend()
plt.ylabel("$I/I_{0}$")
plt.xlabel("frequency (Hz)")

print("mean = %f " % popt[1])
print("sigma(mean) = %f " % perr[1])

plt.show()
