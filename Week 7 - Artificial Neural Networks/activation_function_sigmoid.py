# -*- coding: utf-8 -*-

"""
 
"""

import numpy as np
import numpy.matlib 
import matplotlib.pyplot as plt

# Sigmoid function
def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

# Derivation
def dsigmoid(x):
    return sigmoid(x)*(1.0-sigmoid(x))

# Get some data
x = np.linspace(-5,5)

# Do the plots
fig, ax = plt.subplots(2,1)
ax[0].plot(x, sigmoid(x), lw=2.5, label='Sigmoid')
ax[0].grid()
ax[0].set_xlabel('Input')
ax[0].set_ylabel('Output')
ax[0].legend()
ax[1].plot(x, dsigmoid(x), lw=2.5, c='red', label='Derivative')
ax[1].grid()
ax[1].set_xlabel('Input')
ax[1].set_ylabel('Output')
ax[1].legend()
fig.tight_layout()

