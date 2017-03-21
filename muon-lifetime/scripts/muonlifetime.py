import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

#for bold math
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

#def muonFit(t,C,tau,A1,tau1,A2,tau2):
#    return C*np.exp(-t/tau) + A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)

def muonFit(t,A1,tau1,A2,tau2):
    return 11. + A1*np.exp(-t/tau1) + A2*np.exp(-t/tau2)

def expon(t,A,tau):
    return A*np.exp(-t/tau)

#p_0 = [1000,2,1000,2,10000,2]
p_0 = [1000,2,10000,2]

binnum = []
tbins  = []
fitbnum  = []
fittbins = []

TACbin = 1

CalFac = 0.0105898268 # TAC-->us conversion factor [unit us/TAC]
#CalFac = 10/2048 # TAC-->us conversion factor [unit us/TAC]


with open("../data/decay/mu_dacay_run4_mar20.txt",newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="=")
         for row in reader:
              usbin = TACbin*CalFac
              binnum.append(usbin)
              tbin = float(row[0])
              tbins.append(tbin)
              if TACbin > 30 and TACbin < 2300:
              #if TACbin > 250 and TACbin < 1500:
                  fitbnum.append(usbin)
                  fittbins.append(tbin)
              TACbin += 1

t  = np.linspace(30*CalFac,1975*CalFac,num=2000)
#t1 = np.linspace(68*CalFac,200*CalFac,num=2000)
#t2 = np.linspace(68*CalFac,1800*CalFac,num=2000)

#fit the data
popt, pcov = curve_fit(muonFit,fitbnum,fittbins,p0=p_0)
perr = np.sqrt(np.diag(pcov))
#const = [popt[0]]*len(t)
const = [11.]*len(t)

plt.gcf().set_size_inches(15,5)
plt.ylim([1,1.0e5])
#plt.xlim([0,2050])
plt.xlabel(r'\textbf{Time} [$\mu s$]',size=22,fontweight='bold')
plt.ylabel(r'\textbf{Number of Hits}',size=22,fontweight='bold')
plt.grid(True, which='both')
#plt.plot(binnum,tbins)
#plt.plot(t,muonFit(t,*popt),label='fit')
plt.semilogy(binnum,tbins,color='blue',label='data')
plt.semilogy(t,muonFit(t,*popt),color='magenta',label='fit')
plt.semilogy(t,expon(t,popt[0],popt[1]),color='red',label='exp comp 1')
plt.semilogy(t,expon(t,popt[2],popt[3]),color='black',label='exp comp 2')
#plt.semilogy(t,expon(t,popt[4],popt[5]),color='green',label='exp comp 3')
plt.semilogy(t,const,color='green',label='const comp')
plt.legend(loc=1)
#plt.text(2.,1.e+4,r'\textbf{lifetimes: %f, %f, %f} $\mu s$' % (popt[1],popt[3],popt[5]), ha='left', va='center',fontsize=16,fontweight='bold')
plt.text(2.,1.e+4,r'\textbf{lifetimes: %f, %f} $\mu s$' % (popt[1],popt[3]), ha='left', va='center',fontsize=16,fontweight='bold')

#print("C = %f, A1 = %f, tau1 = %f, A2 = %f, tau2 = %f" % (popt[0],popt[1],popt[2],popt[3],popt[4]))
#print("\u03C3(C) = %f, \u03C3(A1) = %f, \u03C3(tau1) = %f, \u03C3(A2) = %f, \u03C3(tau2) = %f" % (perr[0],perr[1],perr[2],perr[3],perr[4]))

#print("lifetimes = %f, %f, %f" % (popt[1],popt[3],popt[5]))
print("lifetimes = %f, %f" % (popt[1],popt[3]) )

plt.show()

