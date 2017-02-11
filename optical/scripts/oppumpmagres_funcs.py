import math

# define constants
mu_b = 5.7883818012e-5 # bohr magneton [unit ev/T]
gs = 2.0023193043622   # gyromagnetic ratio - spin
gl = 0.99999354        # gyromagnetic ratio - angular
gi = -0.000293640      # gyromagnetic ratio - nuclear
hbar = 4.135667e-15    # [unit ev.s]
mu_o = 1.2566370614e-6 # magnetic vaccum permeability [uni T*m/A]
# approximate magnetic field [T] of the earth according to
# https://www.ngdc.noaa.gov/geomag-web/#igrfwmm
B_earth = 51.7035e-6  # [unit T]

# got this number from Niv's report. Please double check the number
N_A_coil = 110    # number of turns in Maxwell Coil A
N_B_coil = 142    #            ''                   B
N_C_coil = 110    #            ''                   C

x_A_coil = 0.262     # distance to the plane of the coil B [unit: m]
x_B_coil = 0.0       #            ''
x_C_coil = 0.262     #            ''

R_A_coil = 0.591/2.0 # radius of the Maxwell coil A [unit: m]
R_B_coil = 0.784/2.0 #              ''            B
R_C_coil = 0.591/2.0 #              ''            C

# g-factor calculation in weak b-field limit
def calc_gj(j, l, s = 0.5):
    gj = gl*(j*(j+1) - s*(s+1) + l*(l+1))*1.0/(2*j+1) + \
            gs*(j*(j + 1) + s*(s + 1) - l*(l + 1))*1.0/(2*j*(j + 1))
    return gj

def calc_gf(f, i, j, l):
    gj = calc_gj(j,l,)
    gf = gj*(f*(f + 1) - i*(i + 1) + j*(j + 1))*1.0/(2*f*(f + 1)) + \
            gi*(f*(f + 1) + i*(i + 1) - j*(j + 1))*1.0/(2*f*(f + 1))
    return gf

# zeeman splitting energy shift in weak b-field limit with B_ext 
# [unit: ev .. ? ]  <--- Double check this 
def delta_E_hf_weak(gf, b_ext):
    delta_E_hf = gf * (mu_b) * b_ext # / hbar <- lab manual has this ...  
    return delta_E_hf

# convert ev to freq [unit: hz] 
def ev2freq(ev):
    return ev * (2.41804*10.0e14) #hz

# covert freq to ev [input unit: hz]
def freq2ev(freq):
    return freq * (4.135667516 * (10 ** -15))

# convert synthesizer voltage to output function frequency
def VtoFreq(V,mid_f,step_f,num_f):
    return (V/10.0)*(num_f*step_f)+mid_f-step_f*(num_f/2)

# fitting functions for resonance plots
def gauss_function(x,a,x0,sigma):
    return 1 - a*np.exp(-(x-x0)**2/(2.0*sigma**2))

def lorentzian_function(x,a,x0,sigma):
    return 1 - a*(0.5*sigma)/((x-x0)**2+0.25*(sigma)**2)

# given the resonance frequency and g-factor, compute the external B field in weak field limit
def B_ext_weak(gf, freq):
    delta_E = freq2ev(freq)
    return delta_E / (gf * mu_b) #[unit: T]

def B_ext_strong(gj, gi, freq):
    delta_E = freq2ev(freq)
    return detla_E / ((gj + gi) * mu_b)

# calc the field strength paramter x
def calc_x(gj, gi, delta_E_HF, B_ext):
    return math.abs(((gj-gi) * mu_b * B_ext) / delta_E_HF)

def BperI_coil(N, x, R):
    ''' 
        calculate the B field per unit current due to single coil
        input:
            N: number of turns of coil
            x: distance between the center of the coil and the target [unit: m]
            R: radius of coil [unit: m]
        output:
            B_coil/I: Coil B field per unit current [unit: T/A]
    '''
    return (mu_o * N * (R**2))/(2.0 * (x**2 + R**2)**(1.5))

def BperI_maxwell(N_A, x_A, R_A, N_B, x_B, R_B, N_C, x_C, R_C):
    '''
        calculate the B field per unit current due to single coil
        input:
            N: number of turns of coil
            x: distance between the center of the coil and the target [unit: m]
            R: radius of coil [unit: m]
        output:
            B_maxwell/I: Coil B field per unit current [unit: T/A]
    '''
    return BperI_coil(N_A, x_A, R_A) + BperI_coil(N_B, x_B, R_B) + BperI_coil(N_C, x_C, R_C)

def B_ext_net(B_per_I, I_coil, B_ambient):
    '''
        calculate the net B field
        input:
            B_per_I: B field per unit current I of maxwell coils [unit: T/A]
            I_coil : current on maxwell coils [unit: A]
            B_ambiant: ambient B_field [unit: T]
    '''
    return (B_per_I * I_coil) + B_ambient 







