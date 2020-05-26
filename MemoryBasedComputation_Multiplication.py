'''
Summary
This script contains functions to do multiplication using a memory based computation approach
'''
from tqdm import tqdm

# Operation Methods
def Multiply_MemoryBased(a, b, Memory, n): # Memory must have size 2^n x 2^n
    ''' Multiplication Operation using memory method '''

    modVal = (1 << n) - 1   # This is 2**n - 1      # a & modVal = a % len(Memory)

    #print(a, "-", b)
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
        #print("1val1:", val)
        return val

    elif ((a <= len(Memory) and b > len(Memory)) or (a > len(Memory) and b <= len(Memory))):    # case = 2
        #print("Case: 2")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> n), y, Memory, n) << n)
        #print("2val1:", val)
        val += Multiply_MemoryBased((x & modVal), y, Memory, n)
        #print("2val2:", val)
        return val

    elif a > len(Memory) and b > len(Memory):   # case = 3
        #print("Case: 3")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> n), (y >> n), Memory, n) << (2*n))
        #print("3val1:", val)
        val += (Multiply_MemoryBased((x >> n), (y & modVal), Memory, n) << n)
        #print("3val2:", val)
        val += (Multiply_MemoryBased((y >> n), (x & modVal), Memory, n) << n)
        #print("3val3:", val)
        val += Multiply_MemoryBased((x & modVal), (y & modVal), Memory, n)
        #print("3val4:", val)
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

x = 6
ntestcases = 1000
operandRange = (1, 2**x * 10)
Memory = CreateMultiplicationMemory(2**x)

# print("Ans:", Multiply_MemoryBased(570, 13, Memory, n))
# quit()

print("Creating Operands...")
A = []
B = []
for i in tqdm(range(ntestcases)):
    A.append(random.randint(operandRange[0], operandRange[1]))
    B.append(random.randint(operandRange[0], operandRange[1]))
print("Created Operands")

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

print("Not Matches:", notMatchCount)
print("Computed")