# -*- coding: utf-8 -*-

"""
 
"""

import numpy as np
import numpy.matlib 
import matplotlib.pyplot as plt

# ReLU function
def relu(x):
    return np.maximum(0.0, x)

# Derivation
def drelu(x):
    return [1.0 if v > 0 else 0.0 for v in x]

# Get some data
x = np.linspace(-5,5)

# Do the plots
fig, ax = plt.subplots(2,1)
ax[0].plot(x, relu(x), lw=2.5, label='ReLU')
ax[0].grid()
ax[0].set_xlabel('Input')
ax[0].set_ylabel('Output')
ax[0].legend()
ax[1].plot(x, drelu(x), lw=2.5, c='red', label='Derivative')
ax[1].grid()
ax[1].set_xlabel('Input')
ax[1].set_ylabel('Output')
ax[1].legend()
fig.tight_layout()

