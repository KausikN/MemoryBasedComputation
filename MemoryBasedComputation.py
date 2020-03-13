'''
Summary
This script contains functions to do any operation using a memory based computation approach
'''
import MemoryLibrary

from tqdm import tqdm

# Operation Methods
def Operation_MemoryBased(a, b, Memory, n, ZeroMemory): # Memory must have size 2^n x 2^n
    ''' Operation using memory method '''

    #print(a, "-", b)
    # Check for zero
    if a == 0:
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

    #print("Case:", case)

    if case == 1:
        val = Memory[a-1][b-1]
        #print("1val1:", val)
        return Memory[a-1][b-1]

    elif case == 2:
        x, y = max(a, b), min(a, b)
        val = (Operation_MemoryBased(int(x / len(Memory)), y, Memory, n, ZeroMemory) << n)
        #print("2val1:", val)
        val += Operation_MemoryBased((x % len(Memory)), y, Memory, n, ZeroMemory)
        #print("2val2:", val)
        # x . y = len(Memory) . integer of (x / len(Memory)) . y  +  (x % len(Memory)) . y
        return val

    elif case == 3:
        x, y = max(a, b), min(a, b)
        val = (Operation_MemoryBased(int(x / len(Memory)), int(y / len(Memory)), Memory, n, ZeroMemory) << (2*n))
        #print("3val1:", val)
        val += (Operation_MemoryBased(int(x / len(Memory)), (y % len(Memory)), Memory, n, ZeroMemory) << n)
        #print("3val2:", val)
        val += (Operation_MemoryBased(int(y / len(Memory)), (x % len(Memory)), Memory, n, ZeroMemory) << n)
        #print("3val3:", val)
        val += Operation_MemoryBased((x % len(Memory)), (y % len(Memory)), Memory, n, ZeroMemory)
        #print("3val4:", val)
        return val

# Driver Code
import random

n = 6
ntestcases = 1000
operation = 'm'
operandRange = (1, 2**n * 10)
Memory = MemoryLibrary.CreateMemory_BasicOperation(2**n, operation)
ZeroMemory = MemoryLibrary.CreateZeroMemory_BasicOperation(2**n, operation)

# print("Ans:", Operation_MemoryBased(400, 256, Memory, n, ZeroMemory))
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
for i in tqdm(range(ntestcases)):
    NormalOperation.append(MemoryLibrary.BasicOperation(A[i], B[i], operation))
    #print("Normal Operation:", A[i], "x", B[i], "=", NormalOperation[i])
    MemoryOperation.append(Operation_MemoryBased(A[i], B[i], Memory, n, ZeroMemory))
    #print("Memory Operation:", A[i], "x", B[i], "=", MemoryOperation[i])
    if not (NormalOperation[i] == MemoryOperation[i]):
        print("Not Matching:", A[i], operation, B[i], "= Norm:", NormalOperation[i], "Mem:", MemoryOperation[i])
print("Computed")



        
        
    