"""
Functions to do any operation using a memory based computation approach
"""

# Imports
import random
from tqdm import tqdm

from Library.MemoryLibrary import *

# Main Functions
# Operation Functions
def MemoryBasedCompute_Multiply(A, B, Memory, N):
    '''
    Multiplication Operation using Memory Method

    Memory must have size (2^N, 2^N)
    '''
    # Init
    len_M = Memory.shape[0]
    modVal = (1 << N) - 1 # This is (2**N-1) used for (A & modVal) = (A % len_M)
    # print(a, "-", b)
    # Check Base Cases
    if A == 0 or B == 0:
        return 0
    if A == 1:
        return B
    elif B == 1:
        return A
    # Check Cases
    # Case A
    if A <= len_M and B <= len_M:
        # print("Case: A")
        val = Memory[A, B]
        # print("Aval1:", val)
    # Case B
    elif ((A <= len_M and B > len_M) or (A > len_M and B <= len_M)):
        # print("Case: B")
        X, Y = max(A, B), min(A, B)
        val = (MemoryBasedCompute_Multiply((X >> N), Y, Memory, N) << N)
        # print("Bval1:", val)
        val += MemoryBasedCompute_Multiply((X & modVal), Y, Memory, N)
        # print("Bval2:", val)
    # Case C
    elif A > len_M and B > len_M:
        # print("Case: C")
        X, Y = max(A, B), min(A, B)
        val = (MemoryBasedCompute_Multiply((X >> N), (Y >> N), Memory, N) << (2*N))
        # print("Cval1:", val)
        val += (MemoryBasedCompute_Multiply((X >> N), (Y & modVal), Memory, N) << N)
        # print("Cval2:", val)
        val += (MemoryBasedCompute_Multiply((Y >> N), (X & modVal), Memory, N) << N)
        # print("Cval3:", val)
        val += MemoryBasedCompute_Multiply((X & modVal), (Y & modVal), Memory, N)
        # print("Cval4:", val)

    return val