"""
Functions to do multiplication using a memory based computation approach
"""

# Imports
import random
from tqdm import tqdm

# Main Functions
# Utils Functions
def AddTimes(t1, t2):
    '''
    Adds two time dictionaries
    '''
    t_a = {}
    for k in t1.keys():
        t_a[k] = t1[k] + t2[k]
    
    return t_a

# Operation Functions
def Multiply_MemoryBased(a, b, Memory, N):
    '''
    Multiplication Operation using memory method

    Memory must have size 2^N x 2^N
    '''
    # Init
    modVal = (1 << N) - 1   # This is 2**N - 1      # a & modVal = a % len(Memory)
    time = {
        "comp": 0,
        "multiplexer": 0,
        "add": 0,
        "memory": 0,
        "shift": 0,
        "mask": 0
    }
    # # Check for zero
    # if a == 0 or b == 0:
    #     return 0, time
    # if a == 1:
    #     return b, time
    # elif b == 1:
    #     return a, time
    # Time for check case
    ## 2 parallell comparisons (a > len(Memory), b > len(Memory)) (1 comparison delay)
    ## Multiplexer to activate that particular case - 1 multiplexer delay
    time["comp"] += 1
    time["multiplexer"] += 1
    # Check Case
    if a <= len(Memory) and b <= len(Memory):   # case = 1
        #print("Case: 1")
        val = Memory[a-1][b-1]
        # Time for Case 1
        time["memory"] += 1
    elif ((a <= len(Memory) and b > len(Memory)) or (a > len(Memory) and b <= len(Memory))):    # case = 2
        #print("Case: 2")
        x, y = max(a, b), min(a, b)
        term1, time1 = Multiply_MemoryBased((x >> N), y, Memory, N)
        term1 = (term1 << N)
        term2, time2 = Multiply_MemoryBased((x & modVal), y, Memory, N) # Remainder
        val = term1 + term2
        # Time for Case 2
        ## k time
        time = AddTimes(time, time1)
        ## Remainder Memory Access
        time["memory"] += 1
        ## Shift time
        time["shift"] += 1
        # Mask time
        time["mask"] += 1
        ## Add time
        time["add"] += 1
    elif a > len(Memory) and b > len(Memory):   # case = 3
        #print("Case: 3")
        x, y = max(a, b), min(a, b)
        term1, time1 = Multiply_MemoryBased((x >> N), (y >> N), Memory, N)
        term1 = (term1 << (2*N))
        term2, time2 = Multiply_MemoryBased((x >> N), (y & modVal), Memory, N)
        term2 = (term2 << N)
        term3, time3 = Multiply_MemoryBased((y >> N), (x & modVal), Memory, N)
        term3 = (term3 << N)
        term4, time4 = Multiply_MemoryBased((x & modVal), (y & modVal), Memory, N) # Remainder
        val = term1 + term2 + term3 + term4
        # Time for Case 2
        ## Term 1
        time = AddTimes(time, time1)
        ## Term 2
        time = AddTimes(time, time2)
        ## Term 3
        time = AddTimes(time, time3)
        ## Remainder Memory Access
        time["memory"] += 1
        ## Shift time
        time["shift"] += 2
        # Mask time
        time["mask"] += 2
        ## Add time
        time["add"] += 3
        
    return val, time

def CreateMultiplicationMemory(N):
    '''
    Creates Multiplication Memory Matrix of size N*N
    '''
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append((i+1)*(j+1))
        matrix.append(row)

    return matrix

########################################################################################################################
# Custom Case
# Params
x = 4
A = (2**32) - 1
B = (2**32) - 1
# Params

# RunCode
Memory = CreateMultiplicationMemory(2**x)
Value, Time = Multiply_MemoryBased(A, B, Memory, x)
print(A, "x", B, "=", Value)
print()
print(Time)

########################################################################################################################
# # RunCode
# # Params
# x = 6                                       # Creates Memory of size 2^x
# ntestcases = 1000                           # Number of test cases to check
# operandRange = (1, 2**x * 10)               # Range of the randomly generated operands

# # Generate the Memory Matrix
# Memory = CreateMultiplicationMemory(2**x)

# # Create the Operands
# print("Creating Operands...")
# A = []
# B = []
# for i in tqdm(range(ntestcases)):
#     A.append(random.randint(operandRange[0], operandRange[1]))
#     B.append(random.randint(operandRange[0], operandRange[1]))
# print("Created Operands")

# # Compute the products and evaluate
# print("Computing...")
# NormalOperation = []
# MemoryOperation = []
# notMatchCount = 0
# for i in tqdm(range(ntestcases)):
#     NormalOperation.append(A[i] * B[i])
#     print("Normal Operation:", A[i], "*", B[i], "=", NormalOperation[i])
#     MemoryOperation.append(Multiply_MemoryBased(A[i], B[i], Memory, x))
#     print("Memory Operation:", A[i], "*", B[i], "=", MemoryOperation[i])
#     if not (NormalOperation[i] == MemoryOperation[i]):
#         print("Not Matching:", A[i], "*", B[i], "= Norm:", NormalOperation[i], "Mem:", MemoryOperation[i])
#         notMatchCount += 1

# print("Number of Errors:", notMatchCount)
# print("Computed")