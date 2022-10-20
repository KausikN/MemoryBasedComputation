"""
Functions to do any operation using a memory based computation approach
"""

# Imports
import random
from tqdm import tqdm

import MemoryLibrary

# Main Functions
# Operation Functions
def Multiply_MemoryBased(a, b, Memory, N):
    '''
    Multiplication Operation using memory method

    Memory must have size 2^N x 2^N
    '''
    # Init
    modVal = (1 << N) - 1   # This is 2**N - 1      # a & modVal = a % len(Memory)
    # print(a, "-", b)
    # Check for zero
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    elif b == 1:
        return a
    # Check Case
    if a <= len(Memory) and b <= len(Memory):   # case = 1
        # print("Case: 1")
        val = Memory[a-1][b-1]
        # print("1val1:", val)
    elif ((a <= len(Memory) and b > len(Memory)) or (a > len(Memory) and b <= len(Memory))):    # case = 2
        # print("Case: 2")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> N), y, Memory, N) << N)
        # print("2val1:", val)
        val += Multiply_MemoryBased((x & modVal), y, Memory, N)
        # print("2val2:", val)
    elif a > len(Memory) and b > len(Memory):   # case = 3
        # print("Case: 3")
        x, y = max(a, b), min(a, b)
        val = (Multiply_MemoryBased((x >> N), (y >> N), Memory, N) << (2*N))
        # print("3val1:", val)
        val += (Multiply_MemoryBased((x >> N), (y & modVal), Memory, N) << N)
        # print("3val2:", val)
        val += (Multiply_MemoryBased((y >> N), (x & modVal), Memory, N) << N)
        # print("3val3:", val)
        val += Multiply_MemoryBased((x & modVal), (y & modVal), Memory, N)
        # print("3val4:", val)

    return val

def Operation_MemoryBased(a, b, Memory, N, ZeroMemory):
    '''
    Operation using memory method

    Memory must have size 2^N x 2^N
    '''
    # Init
    # print(a, "-", b)
    # Check for zero
    if a == 0 or b == 0:
        return ZeroMemory[1][b]
    elif b == 0:
        return ZeroMemory[0][a]
    # Check Case
    case = None
    # if case 1 - a < len(Memory) and b < len(Memory)
    # if case 2 - a < len(Memory) and b > len(Memory) or a > len(Memory) and b < len(Memory)
    # if case 3 - a > len(Memory) and b > len(Memory)
    if a <= len(Memory) and b <= len(Memory):
        case = 1
    elif ((a <= len(Memory) and b > len(Memory)) or (a > len(Memory) and b <= len(Memory))):
        case = 2
    elif a > len(Memory) and b > len(Memory):
        case = 3
    # print("Case:", case)
    if case == 1:
        val = Memory[a-1][b-1]
        # print("1val1:", val)
    elif case == 2:
        x, y = max(a, b), min(a, b)
        val = (Operation_MemoryBased(int(x / len(Memory)), y, Memory, N, ZeroMemory) << N)
        # print("2val1:", val)
        val += Operation_MemoryBased((x % len(Memory)), y, Memory, N, ZeroMemory)
        # print("2val2:", val)
        # x . y = len(Memory) . integer of (x / len(Memory)) . y  +  (x % len(Memory)) . y
    elif case == 3:
        x, y = max(a, b), min(a, b)
        val = (Operation_MemoryBased(int(x / len(Memory)), int(y / len(Memory)), Memory, N, ZeroMemory) << (2*N))
        # print("3val1:", val)
        val += (Operation_MemoryBased(int(x / len(Memory)), (y % len(Memory)), Memory, N, ZeroMemory) << N)
        # print("3val2:", val)
        val += (Operation_MemoryBased(int(y / len(Memory)), (x % len(Memory)), Memory, N, ZeroMemory) << N)
        # print("3val3:", val)
        val += Operation_MemoryBased((x % len(Memory)), (y % len(Memory)), Memory, N, ZeroMemory)
        # print("3val4:", val)

    return val

# RunCode
# Params
N = 6
ntestcases = 1000
operation = 'm'
operandRange = (1, 2**N * 10)
Memory = MemoryLibrary.CreateMemory_BasicOperation(2**N, operation)
ZeroMemory = MemoryLibrary.CreateZeroMemory_BasicOperation(2**N, operation)
# print("Ans:", Multiply_MemoryBased(570, 13, Memory, N))
# quit()
# Params

# RunCode
# Create Operands
print("Creating Operands...")
A = []
B = []
for i in tqdm(range(ntestcases)):
    A.append(random.randint(operandRange[0], operandRange[1]))
    B.append(random.randint(operandRange[0], operandRange[1]))
print("Created Operands")
# Compute
print("Computing...")
NormalOperation = []
MemoryOperation = []
notMatchCount = 0
for i in tqdm(range(ntestcases)):
    NormalOperation.append(MemoryLibrary.BasicOperation(A[i], B[i], operation))
    print("Normal Operation:", A[i], "x", B[i], "=", NormalOperation[i])
    MemoryOperation.append(Multiply_MemoryBased(A[i], B[i], Memory, N))
    print("Memory Operation:", A[i], "x", B[i], "=", MemoryOperation[i])
    if not (NormalOperation[i] == MemoryOperation[i]):
        print("Not Matching:", A[i], operation, B[i], "= Norm:", NormalOperation[i], "Mem:", MemoryOperation[i])
        notMatchCount += 1
    #Multiply_MemoryBased(A[i], B[i], Memory, N)
# Evaluate
print("Mismatch Count:", notMatchCount)