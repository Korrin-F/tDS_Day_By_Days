# -*- coding: utf-8 -*-

"""
 
"""

import numpy as np
import numpy.matlib 

# Assume these two network layers
input_layer = 50   #number of neurons
hidden_layer = 25  #number of neurons

# Random weights drom Gaussian distribution (mean = 0, variance = 1)
W1 = np.random.randn(hidden_layer, input_layer)

# Weights normalisation: He
W1 = W1 * np.sqrt(1 / hidden_layer)

