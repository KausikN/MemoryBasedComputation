"""
Functions to create and operate on memory for various operations like multiplication, etc
"""

# Imports
import numpy as np

from .OperationLibrary import *

# Main Functions
# Memory Creation Functions
def CreateMemory_CustomOperation(N, operation):
    '''
    Creates CustomOperation (N, N) Memory
    '''
    Memory = np.zeros((N+1, N+1), dtype=int)
    for i in range(Memory.shape[0]):
        for j in range(Memory.shape[1]):
            Memory[i, j] = operation(i, j)
        
    return Memory