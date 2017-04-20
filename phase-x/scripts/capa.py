import numpy as np
import math  

#define variables
freq     = 10.                           # [unit: kHz]
omega    = 2 * np.pi * (freq * 10**3)    # angular frequency [unit: rad/sec]
R_int    = 50.                           # lock-in internal resistance [unit: ohm]
R_add    = 1000.                         # additional resistance [unit: ohm]
R    = R_int + R_add
V_o      = 1.                            # [unit: V]

# define helper functions
def compute_cap(omega, R, Vo, V_meas):
    delta = V_meas/Vo
    return 1/(omega*R)*(1-math.sqrt(1-4*delta**2))/(2*delta)


#def compute_cap2(omega, R, Vo, V_meas):
#    delta = (Vo/V_meas)
#    return math.sqrt(delta**2 - 1)/(R*omega)


print compute_cap(omega, R, V_o, 0.0333) * 10**9
#print compute_cap2(omega, R, V_o, 0.9622) * 10**9






