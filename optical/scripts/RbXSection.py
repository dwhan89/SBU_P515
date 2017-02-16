import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# to calculate number density from temperature
def numDensity(temp):
    n = 101325.0*(10**(4.857-4215/temp))/(1.38*(10**-23)*temp) #[Pa]
    return n;

def exp(x,a,b,c):
    return a*np.exp(-b*x)+c

def linear(x,a,b):
    return a+b*x

I_data = []
n_data = []
maxI = -99999;

# get photodiode voltage (proportional to transmitted intensity)
# vs. temperature data from file and calculate voltage vs.
# number density from it
with open("../data/cell-warmup-heaton.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
     # if row[1] and row[2] exist...?
          I = float(row[1])
          if I > maxI: maxI = I
          t = float(row[2]) + 273.15
          n = numDensity(t)
          I_data.append(I)
          n_data.append(n)

# Normalize intensity
Inorm_data = [x / maxI for x in I_data]
Inormlog_data = [math.log(x) for x in Inorm_data]

#fit the data
popt, pcov = curve_fit(linear,n_data,Inormlog_data)
x = np.linspace(min(n_data),max(n_data), num=1000)
perr = np.sqrt(np.diag(pcov))

# plot I/I_0 vs. n 
plt.scatter(n_data,Inormlog_data)
plt.plot(x,linear(x,*popt))
plt.ylabel("$\ln(I/I_{0})$",size=18,fontweight='bold')
plt.xlabel("Number Density [$m^{-3}$]",size=18)
plt.text(2.3e16,-0.1,r'slope = %.2f $\pm$ %.2f $\times10^{-18}$ m$^{3}$' % (popt[1]*1.0e18,perr[1]*1.0e18), ha='center', va='center',fontweight='bold')
plt.text(2.3e16,-0.11,r'$\sigma$ = %.2f $\pm$ %.2f $\times10^{-17}$ m$^{2}$' % ((popt[1]/0.05)*-1.0e17,(perr[1]/0.05)*1.0e17), ha='center', va='center',fontweight='bold')

plt.show()
