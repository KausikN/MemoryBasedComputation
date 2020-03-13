'''
Summary
This library contains functions to create and operate on memory for various operations like multiplication, etc
'''

# Memory Creation
def CreateMemory_CustomOperation(size, CustomOperation, CustomOperationParameters=None):
    ''' Creates CustomOperation memory of size x size '''
    Memory = []
    for i in range(size):
        MemRow = []
        for j in range(size):
            MemRow.append(CustomOperation((i+1), (j+1), CustomOperationParameters))
        Memory.append(MemRow)
    return Memory

def CreateMemory_BasicOperation(size, operation):
    ''' Creates Operation memory of size x size '''
    operation = operation.lower().strip()
    if operation in ['add', 'addition', 'a']:
        return CreateMemory_Add(size)
    elif operation in ['multiply', 'mul', 'mult', 'm', 'multiplication']:
        return CreateMemory_Multiply(size)
    elif operation in ['sub', 'subtract', 's', 'subtraction']:
        return CreateMemory_Subtract(size)
    elif operation in ['div', 'divide', 'd', 'division']:
        return CreateMemory_Divide(size)

def CreateMemory_Multiply(size):
    ''' Creates multiplication memory of size x size '''
    Memory = []
    for i in range(size):
        MemRow = []
        for j in range(size):
            MemRow.append((i+1) * (j+1))
        Memory.append(MemRow)
    return Memory

def CreateMemory_Add(size):
    ''' Creates addition memory of size x size '''
    Memory = []
    for i in range(size):
        MemRow = []
        for j in range(size):
            MemRow.append((i+1) + (j+1))
        Memory.append(MemRow)
    return Memory

def CreateMemory_Subtract(size):
    ''' Creates subtraction memory of size x size '''
    Memory = []
    for i in range(size):
        MemRow = []
        for j in range(size):
            MemRow.append((i+1) - (j+1))
        Memory.append(MemRow)
    return Memory

def CreateMemory_Divide(size):
    ''' Creates division memory of size x size '''
    Memory = []
    for i in range(size):
        MemRow = []
        for j in range(size):
            MemRow.append((i+1) / (j+1))
        Memory.append(MemRow)
    return Memory

# Operations
def CustomOperation(a, b, CustomOperation, CustomOperationParameters):
    return CustomOperation(a, b, CustomOperationParameters)

def BasicOperation(a, b, operation):
    ''' Does specified operation on a and b '''
    operation = operation.lower().strip()
    if operation in ['add', 'addition', 'a']:
        return a + b
    elif operation in ['multiply', 'mul', 'mult', 'm', 'multiplication']:
        return a * b
    elif operation in ['sub', 'subtract', 's', 'subtraction']:
        return a - b
    elif operation in ['div', 'divide', 'd', 'division']:
        return a / b

# Zero Memory Creation
def CreateZeroMemory_CustomOperation(size, CustomOperation, CustomOperationParameters=None):
    ''' Creates CustomOperation memory of size x size '''
    Memory = []
    MemRow_L = []
    MemRow_R = []
    for i in range(size+1):
        MemRow_L.append(CustomOperation((i), 0, CustomOperationParameters))
        MemRow_R.append(CustomOperation(0, (i), CustomOperationParameters))
    Memory.append(MemRow_L)
    Memory.append(MemRow_R)
    return Memory

def CreateZeroMemory_BasicOperation(size, operation):
    ''' Creates Zero Operation memory of size x size '''
    operation = operation.lower().strip()
    if operation in ['add', 'addition', 'a']:
        return CreateZeroMemory_Add(size)
    elif operation in ['multiply', 'mul', 'mult', 'm', 'multiplication']:
        return CreateZeroMemory_Multiply(size)
    elif operation in ['sub', 'subtract', 's', 'subtraction']:
        return CreateZeroMemory_Subtract(size)
    elif operation in ['div', 'divide', 'd', 'division']:
        return CreateZeroMemory_Divide(size)

def CreateZeroMemory_Multiply(size):
    ''' Creates multiplication Zero memory of size x size '''
    Memory = []
    MemRow_L = []
    MemRow_R = []
    for i in range(size+1):
        MemRow_L.append(0)
        MemRow_R.append(0)
    Memory.append(MemRow_L)
    Memory.append(MemRow_R)
    return Memory

def CreateZeroMemory_Add(size):
    ''' Creates addition Zero memory of size x size '''
    Memory = []
    MemRow_L = []
    MemRow_R = []
    for i in range(size+1):
        MemRow_L.append(i)
        MemRow_R.append(i)
    Memory.append(MemRow_L)
    Memory.append(MemRow_R)
    return Memory

def CreateZeroMemory_Subtract(size):
    ''' Creates subtraction Zero memory of size x size '''
    Memory = []
    MemRow_L = []
    MemRow_R = []
    for i in range(size+1):
        MemRow_L.append(i)
        MemRow_R.append(-(i))
    Memory.append(MemRow_L)
    Memory.append(MemRow_R)
    return Memory

def CreateZeroMemory_Divide(size):
    ''' Creates division Zero memory of size x size '''
    Memory = []
    MemRow_L = []
    MemRow_R = []
    for i in range(size+1):
        MemRow_L.append(None)
        MemRow_R.append(0)
    Memory.append(MemRow_L)
    Memory.append(MemRow_R)
    return Memory