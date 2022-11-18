# -*- coding: utf-8 -*-

"""
 
"""

import numpy as np
import numpy.matlib 

# Assume these two network layers
input_layer = 50   #number of neurons
hidden_layer = 25  #number of neurons

# Random weights with values between 0 and 1
W1 = np.random.uniform(0,1,(hidden_layer, input_layer))

# Weights normalisation =======================================================

# (a) Let's do it for the first row only:
temp_w = W1[0,:]
# (b) Take the sum of this row:
row_sum = np.sum(temp_w)
# (c) Replicate row_sum as many times as the length of temp_w (i.e. input_layer times)
row_sum = np.matlib.repmat(row_sum,1,input_layer)
# (d) Divide each element of temp_w with each element of row_sum
normalised_temp_w = np.divide(temp_w,row_sum)
# (e) Test: sum of normalised_temp_w should be 1
print("Test: First row normalised: ", np.sum(normalised_temp_w))

# Let's now do for all weights in one line of code
W1 = np.divide(W1,np.matlib.repmat(np.sum(W1,1)[:,None],1,input_layer))
print("Test: All rows normalised: ", np.sum(W1,1))