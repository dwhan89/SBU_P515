import oppumpmagres_funcs as func
import numpy as np
import matplotlib.pyplot as plt

# got this number from Niv's report. Please double check the number
N_A = 110    # number of turns in Maxwell Coil A
N_B = 142    #            ''                   B
N_C = 110    #            ''                   C

x_A = 0.262     # distance to the plane of the coil B [unit: m]
x_B = 0.0       #            ''
x_C = 0.262     #            ''

R_A = 0.591/2.0 # radius of the Maxwell coil A [unit: m]
R_B = 0.784/2.0 #              ''            B
R_C = 0.591/2.0 #              ''            C

B_per_I_niv = 2.93e-4 #[unit T/A]
B_per_I     = func.BperI_maxwell(N_A, x_A, R_A, N_B, x_B, R_B, N_C, x_C, R_C) 

print("B field per unit current according to Niv et al. is %f T/A." % (B_per_I_niv))
print("B field per unit current according to our calc is %f T/A." % (B_per_I))
print("the difference between the two value is %f T/A." % (B_per_I - B_per_I_niv))

print("Assume the ambient field of %f T." % (func.B_earth))

B_ext_net_vec = np.vectorize(func.B_ext_net)

I = np.arange(0, 1.0e-3, 1.0e-5)

B_ext = B_ext_net_vec(B_per_I, I, func.B_earth)

I     = I * 1.0e3     # unit conversion from A to mA
B_ext = B_ext * 1.0e3 # unit conversion from T to mT

plt.plot(I, B_ext)
plt.xlabel('Current on Coil [mA]')
plt.ylabel('Net external field [mT]')
plt.title('Net external field due to Maxwell Coil and Ambient field')
plt.show()
