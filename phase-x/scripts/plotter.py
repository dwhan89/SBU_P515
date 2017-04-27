import numpy as np
import matplotlib.pyplot as plt
import os 
import csv

script_path  = os.path.dirname(os.path.realpath(__file__))
data_path    = os.path.join(script_path, "../data")

data_file    = "VO2_Amp_Temp_run1_041117.txt"
path_to_data = os.path.join(data_path, data_file)

if(os.path.isfile(path_to_data)):
    print "loading %s." %(data_file)
    
    with open(path_to_data, 'r') as handle:
        reader = csv.reader(handle, delimiter='\t')
    
        # count the number of lines 
        ctr = 0
        for row in reader:
            ctr += 1
        handle.seek(0)

        data = np.zeros((2, ctr))
        
        for row in reader:



else:
    print "%s does not exists under %s." %(data_file, data_path)
