import matplotlib.pyplot as plt
import csv
import numpy as np

# data setting
input_file = "../data/time_cal/time_calibration_mar7.txt"

# plot setting
#plt.style.use('ggplot')

num_row = 0 
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

plt.figure()
ax = plt.gca()

lbin = 0
plt.plot(data[0][lbin:], data[1][lbin:])
ax.fill_between(data[0][lbin:], data[1][lbin:], 0)
ax.set_ylim([0,1000])

plt.savefig("test.png")


