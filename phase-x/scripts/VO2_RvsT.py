import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# for bold math
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

# experimental settings
V_0   = 1.   #Volts
R_int = 50.  #Ohms

# arrays of resistance and corresponding temperatures
R_warm = []
T_warm = []
R_cool = []
T_cool = []

def calcR(V0,Vm,Rint):
    Resistance =Rint*V0/(V0-Vm) 
    return Resistance

with open("../data/VO2_Amp_Temp_run1_041117_WARMUP.txt",newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:
        V_meas = float(row[2])               #Volts
        Temp  = float(row[0])                #C
        R = calcR(V_0,V_meas,R_int)/1000.    #kilo-Ohms
        R_warm.append(R)
        T_warm.append(Temp)

with open("../data/VO2_Amp_Temp_run1_041117_COOLDOWN.txt",newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:
        V_meas = float(row[2])               #Volts
        Temp  = float(row[0])                #C
        R = calcR(V_0,V_meas,R_int)/1000.    #kilo-Ohms
        R_cool.append(R)
        T_cool.append(Temp)

plt.gcf().subplots_adjust(bottom=0.15,left=0.15,right=0.95)
plt.scatter(T_warm,R_warm,color='red',label="Warm Up")
plt.scatter(T_cool,R_cool,color='blue',label="Cool Down")
plt.ylabel("Resistance [k$\Omega$]",size=20)
plt.xlabel("Temperature [$^{\circ}$C]",size=20)
plt.legend(fontsize=14)
plt.show()
