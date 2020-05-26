'''
Summary
This script contains functions to do multiplication using a memory based computation approach

Required python modules to run:
tqdm    -   pip install tqdm
random  -   pip install random
'''
from tqdm import tqdm

# Operation Methods
def Multiply_MemoryBased(a, b, Memory, n): # Memory must have size 2^n x 2^n
    ''' Multiplication Operation using memory method '''

    modVal = (1 << n) - 1   # This is 2**n - 1      # a & modVal = a % len(Memory)

    # Check for zero
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    elif b == 1:
        return a

    # Check Case
    if a <= len(Memory) and b <= len(Memory):   # case = 1
        #print("Case: 1")
        val = Memory[a-1][b-1]
        return val

    elif ((a <= len(Memory) and b > len(Memory)) or (a > len(Memory) and b <= len(Memory))):    # case = 2
        #print("Case: 2")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> n), y, Memory, n) << n)
        val += Multiply_MemoryBased((x & modVal), y, Memory, n)
        return val

    elif a > len(Memory) and b > len(Memory):   # case = 3
        #print("Case: 3")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> n), (y >> n), Memory, n) << (2*n))
        val += (Multiply_MemoryBased((x >> n), (y & modVal), Memory, n) << n)
        val += (Multiply_MemoryBased((y >> n), (x & modVal), Memory, n) << n)
        val += Multiply_MemoryBased((x & modVal), (y & modVal), Memory, n)
        return val

def CreateMultiplicationMemory(n):
    ''' Creates Multiplication Memory Matrix of size n*n '''
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i+1)*(j+1))
        matrix.append(row)
    return matrix

# Driver Code
import random

# Parameters
x = 6                                       # Creates Memory of size 2^x
ntestcases = 1000                           # Number of test cases to check
operandRange = (1, 2**x * 10)               # Range of the randomly generated operands

# Generate the Memory Matrix
Memory = CreateMultiplicationMemory(2**x)

# Create the Operands
print("Creating Operands...")
A = []
B = []
for i in tqdm(range(ntestcases)):
    A.append(random.randint(operandRange[0], operandRange[1]))
    B.append(random.randint(operandRange[0], operandRange[1]))
print("Created Operands")

# Compute the products and evaluate
print("Computing...")
NormalOperation = []
MemoryOperation = []
notMatchCount = 0
for i in tqdm(range(ntestcases)):
    NormalOperation.append(A[i] * B[i])
    print("Normal Operation:", A[i], "*", B[i], "=", NormalOperation[i])
    MemoryOperation.append(Multiply_MemoryBased(A[i], B[i], Memory, x))
    print("Memory Operation:", A[i], "*", B[i], "=", MemoryOperation[i])
    if not (NormalOperation[i] == MemoryOperation[i]):
        print("Not Matching:", A[i], "*", B[i], "= Norm:", NormalOperation[i], "Mem:", MemoryOperation[i])
        notMatchCount += 1

print("Number of Errors:", notMatchCount)
print("Computed")