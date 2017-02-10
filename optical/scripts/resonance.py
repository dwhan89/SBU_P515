import math
import oppumpmagres_funcs as func

# g-factor for Rb 87 and Rb 85 in weak b-field limit
gf_87 = func.calc_gf(f=2, i=1.5, j=0.5, l=0)
gf_85 = func.calc_gf(f=3, i=2.5, j=0.5, l=0)

print("gf for Rb85 is %f" % gf_85)
print("gf for Rb87 is %f" % gf_87)

del_E_87 = func.delta_E_zee(gf_87, func.B_earth)
del_E_85 = func.delta_E_zee(gf_85, func.B_earth)

print("Zeeman Energy shift of Rb85 ground state due to Earth B-field is %f nev." % (del_E_85 * (10 ** 9)))
print("Zeeman Energy shift of Rb87 ground state due to Earth B-field is %f nev." % (del_E_87 * (10 ** 9)))

Rb85_res_freq = func.ev2freq(del_E_85) 
Rb87_res_freq = func.ev2freq(del_E_87)

print("zeeman resonant freq of Rb85 is %f Hz" % Rb85_res_freq)
print("zeeman resonant freq of Rb87 is %f Hz" % Rb87_res_freq)
