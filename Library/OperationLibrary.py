"""
Functions for operations like multiplication, etc
"""

# Imports
import numpy as np

# Main Functions
# Operation Functions
def Operation_Add(A, B):
    '''
    Operation - Add
    '''
    return A + B

def Operation_Subtract(A, B):
    '''
    Operation - Subtract
    '''
    return A - B

def Operation_Multiply(A, B):
    '''
    Operation - Multiply
    '''
    return A * B

def Operation_Divide(A, B):
    '''
    Operation - Divide
    '''
    return A / B

# Main Vars
OPERATIONS = {
    "Add": Operation_Add,
    "Subtract": Operation_Subtract,
    "Multiply": Operation_Multiply,
    "Divide": Operation_Divide
}