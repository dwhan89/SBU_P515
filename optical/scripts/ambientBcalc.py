import math
import numpy
import csv
import oppumpmagres_funcs as func

ambientB_list = []

#with open("../data/feb14/rb87/RB87ambientFieldmeas.txt",newline='') as csvfile:
with open("../data/feb14/rb85/RB85-deltaEDist.txt",newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter="	")
     for row in reader:
          #Ba = float(row[0])*1000000  #in microTesla
          Ba = float(row[0])*1.0e9  #in neV
          ambientB_list.append(Ba)

meanBa = numpy.mean(ambientB_list)
stdBa = numpy.std(ambientB_list)

#print("ambient field = %f +/- %f uT" % (meanBa,stdBa))
print("energy splitting = %f +/- %f neV" % (meanBa,stdBa))
