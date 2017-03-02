import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

datafile = "../data/eff/S2-eff.txt"
eff_list = []
HV_list  = []

with open(datafile,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              eff = float(row[0])
              HV  = abs(float(row[1]))
              eff_list.append(eff)
              HV_list.append(HV)

plt.scatter(HV_list,eff_list)

plt.show()

