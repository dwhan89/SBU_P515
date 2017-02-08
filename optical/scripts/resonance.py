import math 

# approximate Magnetic field of the earth according to  [unit T]              
#https://www.ngdc.noaa.gov/geomag-web/#igrfwmm
B_earth = 51.7035e-6  # [unit T]            

mu_b = 5.7883818012e-5 # bohr magneton [unit ev/T]
gs = 2.0023193043622   # gyromagnetic ratio - spin 
gl = 0.99999354        # gyromagnetic ratio - angular
gi = -0.000293640      # gyromagnetic ratio - nuclear
hbar = 4.135667e-15    #[unit ev.s]

# g-factor calculation in weak b-field limit
def calc_gj(j, l, s = 0.5):
    gj = gl*(j*(j+1) - s*(s+1) + l*(l+1))/(2*j+1) + \
            gs*(j*(j + 1) + s*(s + 1) - l*(l + 1))/(2*j*(j + 1))
    return gj

def calc_gf(f, i, j, l):
    gj = calc_gj(j,l,)    
    gf = gj*(f*(f + 1) - i*(i + 1) + j*(j + 1))/(2*f*(f + 1)) + \
            gi*(f*(f + 1) + i*(i + 1) - j*(j + 1))/(2*f*(f + 1))
    return gf

# g-factor for Rb 87 and Rb 85 in weak b-field limit
gf_87 = calc_gf(f=2, i=1.5, j=0.5, l=0)
gf_85 = calc_gf(f=3, i=2.5, j=0.5, l=0)

print "gf for Rb85 is %f" % gf_85
print "gf for Rb87 is %f" % gf_87


# zeeman splitting energy shift in weak b-field limit with B_ext 
# [unit: ev .. ? ]  <--- Double check this 
def delta_E_zee(gf, b_ext):
    delta_E_zeeman = gf * (mu_b) * b_ext # / hbar <- lab manual has this ...  
    return delta_E_zeeman

del_E_87 = delta_E_zee(gf_87, B_earth)
del_E_85 = delta_E_zee(gf_85, B_earth)

print "Zeeman Energy shift of Rb85 ground state due to Earth B-field is %f nev." % (del_E_85 * (10 ** 9))
print "Zeeman Energy shift of Rb87 ground state due to Earth B-field is %f nev." % (del_E_87 * (10 ** 9))


#convert ev to freq [unit: hz] 
def ev2freq(ev):
    return ev / (4.135667516 * (10 ** -15)) #hz/ev

Rb85_res_freq = ev2freq(del_E_85) 
Rb87_res_freq = ev2freq(del_E_87)

print "zeeman resonant freq of Rb85 is %f Hz" % Rb85_res_freq
print "zeeman resonant freq of Rb87 is %f Hz" % Rb87_res_freq







