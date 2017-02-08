import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# to calculate number density from temperature
def numDensity(temp):
    n = (10**(4.857-4215/temp))/(1.38*(10**-23)*temp)
    return n;

def exp(x,a,b,c):
    #return a*np.exp(-b*x)+c
    return a*x+b*x**2+c

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

#fit the data
popt, pcov = curve_fit(exp,n_data,Inorm_data)
x = np.linspace(min(n_data),max(n_data), num=1000)

# plot I/I_0 vs. n 
plt.scatter(n_data,Inorm_data)
plt.plot(x,exp(x,*popt))
plt.ylabel("$I/I_{0}$")
plt.xlabel("Number Density")
#plt.yscale('log')
# fit to exponential

plt.show()

print(popt)
