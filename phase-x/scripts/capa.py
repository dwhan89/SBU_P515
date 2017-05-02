import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

# for bold math
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

# experimental settings
freq     = 10.                           # [unit: kHz]
omega    = 2 * np.pi * (freq * 10**3)    # angular frequency [unit: rad/sec]
R_int    = 50.                           # lock-in internal resistance [unit: ohm]
R_add    = 1000.                         # additional resistance [unit: ohm]
R    = R_int + R_add
V_o      = 1.                            # [unit: V]

# arrays of resistance and corresponding temperatures
C_warm = []
T_warm = []
C_cool = []
T_cool = []

# define helper functions
def compute_cap(omega, R, Vo, V_meas):
    delta = V_meas/Vo
    return 1/(omega*R)*(1-np.sqrt(1-4*delta**2))/(2*delta)

#def compute_cap2(omega, R, Vo, V_meas):
#    delta = (Vo/V_meas)
#    return math.sqrt(delta**2 - 1)/(R*omega)

#print compute_cap(omega, R, V_o, 0.0333) * 10**9
#print compute_cap2(omega, R, V_o, 0.9622) * 10**9

with open("../data/BaTiO3_Amp_Temp_run2_042017_WARMUP.txt",newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:
        Vmeas = float(row[2]) - 0.7                          #Volts
        Temp  = float(row[0])                                #C
        C = compute_cap(omega,R,V_o,Vmeas)*1.0e9             #nano-Farad
        C_warm.append(C)
        T_warm.append(Temp)

with open("../data/BaTiO3_Amp_Temp_run2_042017_COOLDOWN.txt",newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:
        Vmeas = float(row[2]) - 0.7                          #Volts
        Temp  = float(row[0])                                #C
        C = compute_cap(omega,R,V_o,Vmeas)*1.0e9             #nano-Farad
        C_cool.append(C)
        T_cool.append(Temp)

plt.ylim(0.,1.0) 
plt.gcf().subplots_adjust(bottom=0.15,left=0.15,right=0.95)                                      
plt.scatter(T_warm,C_warm,color='red',label="Warm Up")
plt.scatter(T_cool,C_cool,color='blue',label="Cool Down")
plt.ylabel("Capacitance [nF]",size=20)
plt.xlabel("Temperature [$^{\circ}$C]",size=20)
plt.legend(fontsize=14)
plt.show()

