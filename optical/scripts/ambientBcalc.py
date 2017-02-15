import math
import numpy
import csv
import oppumpmagres_funcs as func

ambientB_list = []

with open("../data/RB87ambientFieldmeas.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
          Ba = float(row[0])*1000000  #in microTesla
          ambientB_list.append(Ba)

meanBa = numpy.mean(ambientB_list)
stdBa = numpy.std(ambientB_list)

print("ambient field = %f +/- %f uT" % (meanBa,stdBa))
