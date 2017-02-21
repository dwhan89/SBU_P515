import math
import numpy as np
import csv
import oppumpmagres_funcs as func
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#for bold math
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

def linear(x,a,b):
    return a+b*x

deltaE85_list = []
appB85_list   = []
#deltaE_relErr = 0.00176702 #from ambient field energy shift distributions
# ^ data shows absolute error is (more or less) constant, not relative error

with open("../data/magmom/rb85/MagMomMeas-Rb85.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
          dE85 = float(row[0])*1.0e9 #[neV]
          B85  = float(row[1])*1.0e6 #[uT]
          deltaE85_list.append(dE85)
          appB85_list.append(abs(B85))

popt85, pcov85 = curve_fit(linear,appB85_list,deltaE85_list)
x85 = np.linspace(min(appB85_list),max(appB85_list), num=1000)
perr85 = np.sqrt(np.diag(pcov85))


#deltaE85_err    = [20*x*deltaE_relErr for x in deltaE85_list] #20 sigma error bars!
deltaE85_err    = [0.001318999*50]*len(deltaE85_list) #50 sigma error bars!

#format plot
plt.axvline(x=0, color='k')
plt.axhline(y=0, color='k')
plt.grid(True, which='both')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel(r"$\Delta$\textbf{E [neV]}",size=22,fontweight='bold')
plt.xlabel(r"$B_{app}$ $[\mu T]$",size=22,fontweight='bold')
plt.margins(0.05)

# put rb85 data on plot
plt.scatter(appB85_list, deltaE85_list,label='$^{85}$Rb data')
plt.errorbar(appB85_list,deltaE85_list,yerr=deltaE85_err,label='50 $\sigma$ error bars',color='black')
plt.plot(x85,linear(x85,*popt85),color='blue',label='$^{85}$Rb fit')
plt.text(20.,0.7,r'\textbf{$^{85}$Rb slope = (%.5f +/- %.5f)} $\times10^{-3}$ $\frac{ev}{T}$' % (popt85[1],perr85[1]), ha='left', va='center',fontsize=16,fontweight='bold')

# ~~~~~~ BEGIN RB87 ~~~~~~

deltaE87_list = []
appB87_list   = []

with open("../data/magmom/rb87/MagMomMeas-Rb87.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
          dE87 = float(row[0])*1.0e9 #[neV]
          B87  = float(row[1])*1.0e6 #[uT]
          deltaE87_list.append(dE87)
          appB87_list.append(abs(B87))

popt87, pcov87 = curve_fit(linear,appB87_list,deltaE87_list)
x87 = np.linspace(min(appB87_list),max(appB87_list), num=1000)
perr87 = np.sqrt(np.diag(pcov87))

#deltaE87_err    = [20*x*deltaE_relErr for x in deltaE87_list] #20 sigma error bars!
deltaE87_err    = [0.001318999*50]*len(deltaE87_list) #50 sigma error bars!

plt.scatter(appB87_list, deltaE87_list,label='$^{87}$Rb data',color='red')
plt.errorbar(appB87_list,deltaE87_list,yerr=deltaE87_err,color='black')
plt.plot(x87,linear(x87,*popt87),label='$^{87}$Rb fit',color='red')
plt.text(20.,0.2,r'\textbf{$^{87}$Rb slope = (%f +/- %f)} $\times10^{-3}$ $\frac{ev}{T}$' % (popt87[1],perr87[1]), ha='left', va='center',fontsize=16,fontweight='bold')



plt.legend(loc=2,fontsize=16)
plt.show()
