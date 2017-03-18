##
# This code doesn't work
##


import matplotlib.pyplot as plt
import csv
import numpy as np
import util as u

# data setting
run_date   = "mar18"
run_number = 4

input_tmp  = "../data/time_cal/time_calibration_{}_run{}.txt"

input_file = u.format_string(input_tmp, run_date, run_number)

# read in the data file
num_row = 0 
print("reading ", input_file)
with open(input_file, newline='') as handle:
    reader = csv.reader(handle, delimiter="=")
    
    # count the number of low
    for row in reader:
        num_row += 1

    handle.seek(0) # rewind the file 
    
    data       = np.zeros((2, num_row))
    data[0][:] = np.arange(0, num_row, dtype=float)

    # store the data
    i = 0
    for row in reader:
        data[1][i] = int(row[0])
        print(i, data[1][i])
        i += 1

