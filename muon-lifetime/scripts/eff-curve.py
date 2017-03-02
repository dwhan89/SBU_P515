import math
import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.optimize import curve_fit

datafile2 = "../data/eff/S2-eff.txt"
eff2_list = []
HV2_list  = []
datafile3 = "../data/eff/S3-eff.txt"
eff3_list = []
HV3_list  = []

with open(datafile2,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              eff2 = float(row[0])
              HV2  = abs(float(row[1]))
              eff2_list.append(eff2)
              HV2_list.append(HV2)

with open(datafile3,newline='') as csvfile:
         reader = csv.reader(csvfile, delimiter="	")
         for row in reader:
         # if row[1] and row[2] exist...?
              eff3 = float(row[0])
              HV3  = abs(float(row[1]))
              eff3_list.append(eff3)
              HV3_list.append(HV3)

plt.scatter(HV2_list,eff2_list,color='red')
plt.scatter(HV3_list,eff3_list,color='blue')

plt.show()

