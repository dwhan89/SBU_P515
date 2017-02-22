import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import oppumpmagres_funcs as func

#for bold math
plt.rc('text', usetex=True)
plt.rcParams['text.latex.preamble'] = [r'\boldmath']

# for converting V --> frequency (Hz)
mid_freq_list = [300e3,360e3,420e3,480e3,540e3,590e3,650e3,710e3,770e3,820e3,880e3,940e3,1000e3,1050e3,1100e3,1160e3,1230e3,1280e3,1340e3,1390e3]
#mid_freq_list  = [945.0e3]*20
step_freq_list = [50]*20
num_freq_list  = [1000]*20
#I_maxwell_list = [-384.0e-3]*20
sig_I_maxwell  = 0.01e-3
#for converting I in maxwell coils to DC B-Field
I_maxwell_list = [-0.00e-3,-20.00e-3,-40.10e-3,-60.10e-3,-79.80e-3,-100.00e-3,-119.70e-3,-140.00e-3,-160.30e-3,-180.50e-3,-200.10e-3,-220.20e-3,-240.20e-3,-260.50e-3,-279.70e-3,-299.90e-3,-320.00e-3,-340.20e-3,-359.70e-3,-380.20e-3] # [unit = A]

#choose  isotope
gf_85 = func.calc_gf(f=3, i=2.5, j=0.5, l=0)
gf_87 = func.calc_gf(f=2, i=1.5, j=0.5, l=0)
#gf = gf_85
gf = gf_87

# for data handling
datafile_list = []
#datafile_base = "../data/4v_err/rb85/rb85-4verr-run"
#datafile_base = "../data/4v_err/rb85/rb85-4verr-run"
datafile_base = "../data/magmom/rb87/rb87-magmom-run"
I_data = []
f_data = []

for j in range(1,21):
    datafile_list.append(datafile_base + str(j) + '.txt')

def calcEvsB(datafile,mid_freq,step_freq,num_freq,I_maxwell):

    #reset variables each time
    I_data = []
    Inorm_data =[]
    f_data = []
    maxI = -99999.
    res_peak = 0.
    res_peak_err = 0.
    deltaE = 0.
    B_maxwell = 0.

    # get photodiode voltage (proportional to transmitted intensity)
    # vs. temperature data from file and calculate voltage vs.
    # number density from it
    with open(datafile,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              I = float(row[1])
              if I > maxI: maxI = I
              V = float(row[0])
              f = func.VtoFreq(V,mid_freq,step_freq,num_freq)
              I_data.append(I)
              f_data.append(f)

    # Normalize intensity
    Inorm_data = [x / maxI for x in I_data]

    #fit the data
    #popt, pcov = curve_fit(gauss_function,f_data,Inorm_data,p0=[0.02,5,2])
    popt, pcov = curve_fit(func.lorentzian_function,f_data,Inorm_data,p0=[0.02,mid_freq,10e3])
    perr = np.sqrt(np.diag(pcov))
    x = np.linspace(min(f_data),max(f_data), num=1000)
    res_peak = popt[1]
    res_peak_err = perr[1]

    fit_string = 'mean = %.2f +/- %.2f Hz' % (res_peak, res_peak_err)

    # plot I/I_0 vs. n 
    plt.plot(f_data,Inorm_data,label='data',color='black')
    #plt.plot(x,func.lorentzian_function(x,*popt),'r-',label='Lorentzian fit')
    #plt.legend()
    plt.ylabel(r"$\frac{I}{I_{0}}$",rotation=0,labelpad=15,size=22,fontweight='bold')
    plt.xlabel(r"\textbf{Frequency [kHz]}",labelpad=10,size=22,fontweight='bold')
    plt.text(296000,1.005,fit_string, ha='center', va='center',fontweight='bold')

    plt.gcf().subplots_adjust(left=0.15)
    plt.gcf().subplots_adjust(bottom=0.12)
    plt.grid(True, which='both')
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.ylim([0.999,1.0001])
    plt.margins(0.05)

    print("mean = %f +- %f Hz" % (res_peak,res_peak_err))
    ambientB = func.B_ext_weak(gf, res_peak)

    print("ambient field = %f T" % ambientB)

    #-------------------------------------
    #UNCOMMENT TO PRINT RESULT TO FILE
    #-------------------------------------
    #outFile = open("../data/4v_err/rb85/highBsigma.txt","a")
    #outFile = open("../data/feb14/rb85/RB85-resPeakDist.txt","a")
    #outFile.write(str(res_peak)+"\n")
    #outFile.close()

    # ~~~ Everything above for ambient field measurement
    # ~~~ Everything below for magnetic moment measurement

    B_per_I = func.MaxwellBperI #[unit T/A]
    B_maxwell = B_per_I*I_maxwell 
    sig_B_maxwell = math.sqrt( (func.sig_MaxwellBperI*I_maxwell)**2 + (sig_I_maxwell*B_maxwell)**2  )

    deltaE = func.freq2ev(res_peak)
    print("maxwell field = %f T" % B_maxwell)
    print("Maxwell B = %f T" % (B_per_I*I_maxwell))

    #-------------------------------------
    #UNCOMMENT TO PRINT RESULT TO FILE
    #-------------------------------------
    outFile = open("../data/magmom/rb87/MagMomMeas-Rb87.txt","a")
    outFile.write(str(deltaE)+"	" + str(B_maxwell) + "	" + str(sig_B_maxwell) + "\n")
    outFile.close()

    #plt.show()
    return


for k in range(0,20):
    calcEvsB(datafile_list[k],mid_freq_list[k],step_freq_list[k],num_freq_list[k],I_maxwell_list[k])

#calcEvsB("../data/multi_splitting/rb85/rb85_multi_splitting.txt",2079.0,20.0e-3,1000,-975.9)

	

