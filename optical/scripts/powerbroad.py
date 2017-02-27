import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit
import oppumpmagres_funcs as func

width_data = []
amp_data = []

with open('../data/power_broadening/width-vs-amp.txt',newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
              hwhm = float(row[0])               # HWHM in Hz
              fwhm = hwhm*2/1000                 # FWHM in kHz
              a = float(row[1])
              width_data.append(fwhm)
              amp_data.append(a)

plt.grid(True, which='both')
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel(r"FWHM [kHz]",size=22,fontweight='bold')
plt.xlabel(r"Power [dB]",size=22,fontweight='bold')
plt.margins(0.05)
plt.gcf().subplots_adjust(bottom=0.125)

plt.scatter(amp_data,width_data,marker='o',color='r')

plt.show()
