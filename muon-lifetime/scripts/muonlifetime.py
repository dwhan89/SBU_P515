import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

#def muonFit(t,C,tau,A1,tau1,A2,tau2):
#    return C*np.exp(-t/tau) + A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)
def muonFit(t,A1,tau1,A2,tau2):
    return A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)


def expon(t,A,tau):
    return A*np.exp(-t/tau)

p_0 = [100,2,100,2]

binnum = []
tbins  = []
fitbnum  = []
fittbins = []

TACbin = 1

CalFac = 0.0053 # TAC-->us conversion factor [unit us/TAC]
#CalFac = 10/2048 # TAC-->us conversion factor [unit us/TAC]


with open("../data/decay/muonlifetime-march10-midrun.txt",newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="=")
         for row in reader:
              usbin = TACbin*CalFac
              binnum.append(usbin)
              tbin = float(row[0])
              tbins.append(tbin)
              if TACbin > 67 and TACbin < 1976:
              #if TACbin > 250 and TACbin < 1500:
                  fitbnum.append(usbin)
                  fittbins.append(tbin)
              TACbin += 1

t  = np.linspace(68*CalFac,1975*CalFac,num=2000)
#t1 = np.linspace(68*CalFac,200*CalFac,num=2000)
#t2 = np.linspace(68*CalFac,1800*CalFac,num=2000)

#fit the data
popt, pcov = curve_fit(muonFit,fitbnum,fittbins,p0=p_0)
perr = np.sqrt(np.diag(pcov))
#const = [popt[0]]*len(t)

plt.gcf().set_size_inches(15,5)
plt.ylim([1,1.0e5])
#plt.xlim([0,2050])
plt.xlabel('Time [$\mu$s]',size=22,fontweight='bold')
plt.ylabel('Number of Hits',size=22,fontweight='bold')
plt.grid(True, which='both')
#plt.plot(binnum,tbins)
#plt.plot(t,muonFit(t,*popt),label='fit')
plt.semilogy(binnum,tbins,color='blue',label='data')
plt.semilogy(t,muonFit(t,*popt),color='magenta',label='fit')
plt.semilogy(t,expon(t,popt[0],popt[1]),color='red',label='exp comp. 1')
plt.semilogy(t,expon(t,popt[2],popt[3]),color='black',label='exp comp 2')
#plt.semilogy(t,expon(t,popt[4],popt[5]),color='green',label='exp comp 3')
plt.legend(loc=1)

#print("C = %f, A1 = %f, tau1 = %f, A2 = %f, tau2 = %f" % (popt[0],popt[1],popt[2],popt[3],popt[4]))
#print("\u03C3(C) = %f, \u03C3(A1) = %f, \u03C3(tau1) = %f, \u03C3(A2) = %f, \u03C3(tau2) = %f" % (perr[0],perr[1],perr[2],perr[3],perr[4]))

#print("lifetimes = %f, %f, %f" % (popt[1],popt[3],popt[5]))
print("lifetimes = %f, %f" % (popt[1],popt[3]) )

plt.show()

