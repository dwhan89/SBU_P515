import math
import numpy as np
import csv
import oppumpmagres_funcs as func
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear(x,a,b):
    return a+b*x

deltaE85_list = []
appB85_list   = []
deltaE_relErr = 0.00176702 #from ambient field energy shift distribution

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

deltaE85_err    = [20*x*deltaE_relErr for x in deltaE85_list] #20 sigma error bars!

plt.scatter(appB85_list, deltaE85_list,label='$^{85}$Rb data')
plt.errorbar(appB85_list,deltaE85_list,yerr=deltaE85_err,label='20 $\sigma$ error bars',color='black')
plt.plot(x85,linear(x85,*popt85),color='blue',label='$^{85}$Rb fit')
plt.ylabel("$\Delta$E [neV]",size=18,fontweight='bold')
plt.xlabel("$B_{app}$ [$\mu$T]",size=18,fontweight='bold')
plt.text(120.,1.25,r'$^{85}$Rb slope = %.5f +/- %.5f $\times10^{-3}$ $\frac{ev}{T}$' % (popt85[1],perr85[1]), ha='center', va='center',fontweight='bold')







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

deltaE87_err    = [20*x*deltaE_relErr for x in deltaE87_list] #20 sigma error bars!


plt.scatter(appB87_list, deltaE87_list,label='$^{87}$Rb data',color='red')
plt.errorbar(appB87_list,deltaE87_list,yerr=deltaE87_err,color='black')
plt.plot(x87,linear(x87,*popt87),label='$^{87}$Rb fit',color='red')
plt.text(115.,0.7,r'$^{87}$Rb slope = %f +/- %f $\times10^{-3}$ $\frac{ev}{T}$' % (popt87[1],perr87[1]), ha='center', va='center',fontweight='bold')



plt.legend(loc=2)
plt.show()
