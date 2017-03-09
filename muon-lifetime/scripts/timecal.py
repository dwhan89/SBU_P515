import matplotlib.pyplot as plt
import csv
import numpy as np
import util as u

# data setting
run_date   = "mar7"
run_number = 2

input_tmp  = "../data/time_cal/time_calibration_{}_run{}.txt"

input_file = u.format_string(input_tmp, run_date, run_number)

# plot setting
lbin = 6

# calibration setting
period     = 2.96  # unit: us
num_period = 3     # the number of full periods in the data set      

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

'''
ctr = 0   # count number of period
i   = lbin

prev_num = 0
cur_num  = 0

sig_start = -1
sig_end   = -1
while(ctr < num_period):
    #print(ctr, i, cur_num, sig_start, sig_end)
    cur_num = data[1][i]

    if(prev_num == 0 and cur_num > 0):
        print("mark ", i)
        if(sig_start < 0):
            sig_start = i
        else:
            ctr +=1
    else:
        pass

    prev_num = cur_num
    i += 1

sig_end = i-1
time_per_bin = (period * num_period) / ((sig_end - sig_start) * 1.0)


print("The number of full periods in the data : ", num_period)
print("period                                 : ", period, " us")
print("the signal starts                      : ", sig_start)
print("the signal ends                        : ", sig_end)
print("time per bin                           : ", time_per_bin, " us/bin")
'''

