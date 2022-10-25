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
    Memory = np.zeros((N+1, N+1), dtype=float)
    for i in range(N):
        for j in range(N):
            Memory[i, j] = operation((i+1), (j+1))
        
    return Memory