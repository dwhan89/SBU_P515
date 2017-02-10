import math

# define constants
mu_b = 5.7883818012e-5 # bohr magneton [unit ev/T]
gs = 2.0023193043622   # gyromagnetic ratio - spin
gl = 0.99999354        # gyromagnetic ratio - angular
gi = -0.000293640      # gyromagnetic ratio - nuclear
hbar = 4.135667e-15    #[unit ev.s]
# approximate magnetic field [T] of the earth according to
# https://www.ngdc.noaa.gov/geomag-web/#igrfwmm
B_earth = 51.7035e-6  # [unit T]

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

# zeeman splitting energy shift in weak b-field limit with B_ext 
# [unit: ev .. ? ]  <--- Double check this 
def delta_E_zee(gf, b_ext):
    delta_E_zeeman = gf * (mu_b) * b_ext # / hbar <- lab manual has this ...  
    return delta_E_zeeman

# convert ev to freq [unit: hz] 
def ev2freq(ev):
    return ev / (4.135667516 * (10 ** -15)) #hz/ev

# convert synthesizer voltage to output function frequency
def VtoFreq(V,mid_f,step_f,num_f):
    return (V/10)*(num_f*step_f)+mid_f-step_f*(num_f/2)

# fitting functions for resonance plots
def gauss_function(x,a,x0,sigma):
    return 1 - a*np.exp(-(x-x0)**2/(2*sigma**2))

def lorentzian_function(x,a,x0,sigma):
    return 1 - a*(0.5*sigma)/((x-x0)**2+0.25*(sigma)**2)
