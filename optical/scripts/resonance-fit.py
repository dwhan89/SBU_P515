import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import oppumpmagres_funcs as func

# for converting V --> frequency (Hz)
mid_freq = 299e3
step_freq = 15
num_freq = 1000

# for data handling
datafile = "../data/feb14/rb87/ambientres-87rb-run1.txt"
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

fit_string = 'mean = %.2f +/- %.2f Hz' % (popt[1], perr[1])

# plot I/I_0 vs. n 
plt.scatter(f_data,Inorm_data,label='data')
plt.plot(x,func.lorentzian_function(x,*popt),'r-',label='Lorentzian fit')
plt.legend()
plt.ylabel("$I/I_{0}$")
plt.xlabel("frequency (Hz)")
plt.text(296000,1.005,fit_string, ha='center', va='center',fontweight='bold')

print("mean = %f Hz" % popt[1])
print("sigma(mean) = %f Hz" % perr[1])

gf_85 = func.calc_gf(f=3, i=2.5, j=0.5, l=0)
gf_87 = func.calc_gf(f=2, i=1.5, j=0.5, l=0)
ambientB = func.B_ext_weak(gf_87, popt[1])

print("ambient field = %f T" % ambientB)

#-------------------------------------
#UNCOMMENT TO PRINT RESULT TO FILE
#-------------------------------------
#outFile = open("../data/RB87ambientFieldmeas.txt","a")
#outFile.write(str(ambientB)+"\n")
#outFile.close()

plt.show()
