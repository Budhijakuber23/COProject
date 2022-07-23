from matplotlib import pyplot as plt
from sys import stdin

pc = 0
memory = []

registerStored = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
}

opcodes = {
    "11010": "xor",
    "11011": "or",
    "11100": "and",
    "11101": "not",
    "11110": "cmp",
    "11111": "jmp",
    "01100": "jlt",
    "01101": "jgt",
    "01111": "je",
    "01010": "hlt",
    "10000": "add",
    "10001": "sub",
    "10010": "movI",
    "10011": "movR",
    "10100": "ld",
    "10101": "st",
    "10110": "mul",
    "10111": "div",
    "11000": "rs",
    "11001": "ls",
}

def convertToDecimal(Bstr):
    num=list(Bstr)
    ans=0
    n=len(num)
    i=0
    while(i!=n):
        if num[n-i-1]=='1':
            ans+=2**i
            i+=1
        else:
            i+=1
            continue
    return ans

def convertToBin(num, bits):
    if num==0:
        return "0" * bits
    else:
        ans=""
        while(num>1):
            solpart=str(num%2)
            ans+=solpart
            num=int(num/2)
    ans="1"+ans

    leftBits= bits - len(ans)
    if (leftBits>0):
        padd="0"* leftBits
        ans=padd+ans
    return ans


def countr_reg(pc):
    print(pc, end=" ")
    for i in registerStored.values():
        print(convertToBin(i, 16), end=" ")
    print()


def memDump(memory):
    x=len(memory)
    for i in range(x):
        print(memory[i])






def sTypeA(inst):
    opcode = inst[0:5]
    desReg = inst[7:10]
    op1 = registerStored[inst[10:13]]
    op2 = registerStored[i[13:]]

    if(opcodes[opcode] == "add"):
        result = op1 + op2
        binaryVal = convertToBin(result, 16)
        if len(binaryVal) > 16:
            binaryVal = binaryVal[-16:]
            registerStored["111"] = 8
            result = convertToDecimal(resInBin)
    elif(opcodes[opcode] == "xor"):
        result = op1 ^ op2

    elif(opcodes[opcode] == "or"):
        result = op1 | op2

    elif(opcodes[opcode] == "and"):
        result = op1 & op2


    elif(opcodes[opcode] == "sub"):
        result = op1 - op2
        if (result < 0):
            result = 0
            registerStored["111"] = 8

    elif(opcodes[opcode] == "mul"):
        result = op1 * op2
        binaryVal = convertToBin(result, 16)
        if len(resInBin) > 16:
            binaryVal = binaryVal[-16:]
            registerStored["111"] = 8
            result = convertToDecimal(resInBin)

    registerStored[desReg] = result


def sTypeB(inst):
    
    opcode = inst[0:5]
    reg = inst[5:8]
    immediate = convertToDecimal(inst[8:])

    if (opcodes[opcode] == "movI"):
        registerStored[reg] = immediate

    elif (opcodes[opcode] == "rs"):
        result = ("0"*immediate) + convertToBin(registerStored[reg], 16)
        result = result[0:16]
        registerStored[reg] = convertToDecimal(result)

    elif (opcodes[opcode] == "ls"):
        result = convertToBin(registerStored[reg], 16) + ("0"*immediate)
        result = result[-16:]
        registerStored[reg] = convertToDecimal(result)


def sTypeC(inst, currFlag):
    opcode = inst[0:5]

    if (opcodes[opcode] == "cmp"):
        val1 = registerStored[inst[10:13]]
        val2 = registerStored[inst[13:]]
        if (val1 < val2):
            registerStored["111"] = 4
        elif (val1 > val2):
            registerStored["111"] = 2
        else:
            registerStored["111"] = 1

    elif (opcodes[opcode] == "not"):
        noToFlip = convertToBin(registerStored[inst[13:]], 16)

        inverting = ""
        xx=len(noToFlip)
        for i in range(x):
            if(noToFlip[i] == "1"):
                inverting += "0"
            else:
                inverting += "1"

        flippedNo = convertToDecimal(inverting)

        registerStored[inst[10:13]] = flippedNo

    elif (opcodes[opcode] == "div"):
        quotient = (registerStored[inst[10:13]]) // (registerStored[inst[13:]])
        remainder = registerStored[inst[10:13]] % registerStored[inst[13:]]
        registerStored["000"] = quotient
        registerStored["001"] = remainder

    elif (opcodes[opcode] == "movR"):
        if(inst[13:] == "111"):
            registerStored[inst[10:13]] = currFlag
            return
        registerStored[inst[10:13]] = registerStored[inst[13:]]


def sTypeD(inst):
    opcode = i[0:5]
    valueToStore = registerStored[i[5:8]]
    valueToLoad = convertToDecimal(memory[location])

    if(opcodes[opcode] == "st"):
        memory[convertToDecimal(i[8:])] = convertToBin(valueToStore, 16)

    elif(opcodes[opcode] == "ld"):
        registerStored[i[5:8]] = valueToLoad


def sTypeE(i, currFlag, progc):
    opcode = i[0:5]
    if(opcodes[opcode] == "jmp"):
        progc = convertToDecimal(i[8:])

    elif (opcodes[opcode] == "jgt"):
        if(currFlag == 2):
            progc = convertToDecimal(i[8:])
        else:
            progc += 1
    elif (opcodes[opcode] == "jlt"):
        if(currFlag == 4):
            progc = convertToDecimal(i[8:])
        else:
            progc += 1
    elif (opcodes[opcode] == "je"):
        if(currFlag == 1):
            progc = convertToDecimal(i[8:])
        else:
            progc += 1

    return progc


x = []
y = []

for line in stdin:

    line = line.strip()


    if line == "s":
        memory.append("1001100000000000")
        break
    memory.append(line)

    if(line == ""):
        continue

xy=len(memory)
while(xy < 256):
    memory.append(convertToBin(0, 16))

cycleNo = 0


stopCode = False
while(pc < xy):

    if stopCode:
        break

    x.append(cycleNo)
    y.append(pc)
    cycleNo += 1

    pc_print = convertToBin(pc, 8)


    currFlagR = registerStored["111"]
    
    currFlagR = registerStored["111"]
    
    registerStored["111"] = 0

    
    op = memory[pc][0:5]

    
    if(opcodes[op] == "hlt"):
        stopCode = True

    if(
        (opcodes[op] == "add") or
        (opcodes[op] == "sub") or
        (opcodes[op] == "mul") or
        (opcodes[op] == "xor") or
        (opcodes[op] == "or") or
        (opcodes[op] == "and")
    ):
        sTypeA(memory[pc])

    elif (
            (opcodes[op] == "cmp") or
            (opcodes[op] == "movR") or
            (opcodes[op] == "div") or
            (opcodes[op] == "not")
         ):
        sTypeC(memory[pc], currFlagR)

    elif(
            (opcodes[op] == "movI") or
            (opcodes[op] == "ls") or
            (opcodes[op] == "rs")
         ):

        sTypeB(memory[pc])

    elif(
            (opcodes[op] == "ld") or
            (opcodes[op] == "st")):
        cycleNo -= 1
        x.append(cycleNo)
        y.append(convertToDecimal(memory[pc][-8:]))
        cycleNo += 1
        sTypeD(memory[pc])

    elif(
            (opcodes[op] == "jmp") or
            (opcodes[op] == "jgt") or
            (opcodes[op] == "jlt") or
            (opcodes[op] == "je")):
        pc = sTypeE(memory[pc], currFlagR, pc)
        countr_reg(pc_print)
        continue

    countr_reg(pc_print)

    pc += 1

memDump(memory)

plt.plot(x, y, 'o')
plt.title('Graph showing the memory locations accessed during different cycles')
plt.xlabel('Cycle No')
plt.ylabel('Memory location acessed')
plt.savefig('graph.png')
