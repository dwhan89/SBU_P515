import matplotlib.pyplot as plt
import csv
import numpy as np
import util as u

# data setting
run_date   = "mar7"
run_number = 2

input_tmp  = "../data/time_cal/time_calibration_{}_run{}.txt"
output_tmp = "../data/plots/time_cal_{}_run{}.png"

input_file = u.format_string(input_tmp, run_date, run_number)
output_file = u.format_string(output_tmp, run_date, run_number)

# plot setting
lbin = 0

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
        data[1][i] = float(row[0])
        i += 1

# plot the image
plt.figure()
ax = plt.gca()

plt.plot(data[0][lbin:], data[1][lbin:])
plt.xlabel("MCA Channel Number")
plt.ylabel("Number of Hits")

ax.fill_between(data[0][lbin:], data[1][lbin:], 0)
ax.set_ylim([0,1000])

print("creating ", output_file)
plt.savefig(output_file)
plt.show()
