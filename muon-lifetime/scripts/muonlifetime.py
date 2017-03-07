import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def muonFit(t,C,A1,tau1,A2,tau2):
    return C + A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)

def expon(t,A,tau):
    return A*np.exp(-t/tau)

p_0 = [20,10000,400,1000,400]

binnum = []
tbins  = []

fitbnum  = []
fittbins = []

currentbin = 1

with open("../data/decay/muonlifetime-march2-7.txt",newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="=")
         for row in reader:
              binnum.append(currentbin)
              tbin = float(row[0])
              tbins.append(tbin)
              if currentbin > 67 and currentbin < 1976:
                  fitbnum.append(currentbin)
                  fittbins.append(tbin)
              currentbin += 1

t  = np.linspace(68,1975, num=2000)
t1 = np.linspace(68,200, num=2000)
t2 = np.linspace(68,1800, num=2000)

#fit the data
popt, pcov = curve_fit(muonFit,fitbnum,fittbins,p0=p_0)

plt.gcf().set_size_inches(15,5)
plt.ylim([1,1.0e5])
plt.xlim([0,2050])
plt.xlabel('Time [TAC]',size=22,fontweight='bold')
plt.ylabel('Number of Hits',size=22,fontweight='bold')
plt.grid(True, which='both')
#plt.plot(binnum,tbins)
#plt.plot(t,muonFit(t,*popt),label='fit')
plt.semilogy(binnum,tbins)
plt.semilogy(t,muonFit(t,*popt),label='fit')
plt.semilogy(t1,expon(t1,popt[1],popt[2]),color='red',label='comp 1')
plt.semilogy(t2,expon(t2,popt[3],popt[4]),color='black',label='comp 2')
plt.legend(loc=1)

print("C = %f, A1 = %f, tau1 = %f, A2 = %f, tau2 = %f" % (popt[0],popt[1],popt[2],popt[3],popt[4]))

plt.show()

