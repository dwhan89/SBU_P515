import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

def muonFit(t,C,A1,tau1,A2,tau2):
    return C + A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)

p_0 = [20,10000,400,1000,400]

binnum = []
tbins  = []

fitbnum  = []
fittbins = []

currentbin = 1

with open("../data/decay/muonlifetime-march2-7PEDREMOVED.txt",newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="=")
         for row in reader:
              binnum.append(currentbin)
              tbin = float(row[0])
              tbins.append(tbin)
              if currentbin > 67 and currentbin < 1976:
                  fitbnum.append(currentbin)
                  fittbins.append(tbin)
              currentbin += 1

t = np.linspace(0,2040, num=1000)

#fit the data
popt, pcov = curve_fit(muonFit,fitbnum,fittbins,p0=p_0)

plt.gcf().set_size_inches(15,5)
plt.xlabel('Time [TAC]',size=22,fontweight='bold')
plt.ylabel('Number of Hits',size=22,fontweight='bold')
plt.grid(True, which='both')
#plt.plot(binnum,tbins)
#plt.plot(t,muonFit(t,*popt),label='fit')
plt.semilogy(binnum,tbins)
plt.semilogy(t,muonFit(t,*popt),label='fit')
plt.legend(loc=2)

print("C = %f, A1 = %f, tau1 = %f, A2 = %f, tau2 = %f" % (popt[0],popt[1],popt[2],popt[3],popt[4]))

plt.show()

