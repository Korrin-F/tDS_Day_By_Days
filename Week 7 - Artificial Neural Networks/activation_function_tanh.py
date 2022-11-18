# -*- coding: utf-8 -*-

"""
 
"""

import numpy as np
import numpy.matlib 
import matplotlib.pyplot as plt

# Tanh function
def tanh(x):
    return (np.exp(x)-np.exp(-x)) / (np.exp(x)+np.exp(-x))

# Derivation
def dtanh(x):
    return 1.0 - (tanh(x)**2)

# Get some data
x = np.linspace(-5,5)

# Do the plots
fig, ax = plt.subplots(2,1)
ax[0].plot(x, tanh(x), lw=2.5, label='Tanh')
ax[0].grid()
ax[0].set_xlabel('Input')
ax[0].set_ylabel('Output')
ax[0].legend()
ax[1].plot(x, dtanh(x), lw=2.5, c='red', label='Derivative')
ax[1].grid()
ax[1].set_xlabel('Input')
ax[1].set_ylabel('Output')
ax[1].legend()
fig.tight_layout()

