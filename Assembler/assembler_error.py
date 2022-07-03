from definations import instructions, labels, StoredRegisters, StoredVars, opcodes

from co_helper import convertToBin
from sys import stdin

from types import typeA, typeB, typeC, typeD, typeE, typeF

result = []
lineNo = 0
halt = False
varDef = False
error = False

for line in stdin:

    inst = line.split()
    if line != "" :

#handling errors
        if halt == True :
            raise Exception(f"Halt should be last instruction! Error in line {lineNo}")

        if len(instructions) == 256 :
            raise Exception(f"Memory Overflow! Error in line {lineNo}")

        if ((inst[0] != "var") and (varDef == False)) :
            varDef = True

        elif ((inst[0] == "var") and (varDef == True)):
            raise Exception(f"Variable should be defined in the begining! Error in line {lineNo}")


#handling labels
        if ":" in line: 
            lIndex = line.index(":")

            if " " in line[0:lIndex] :
                raise Exception(f"Space between label and colon! Error in line {lineNo}")

            name = line[0:lIndex]

            if name in labels.keys() :
                raise Exception(f"Illegal naming of label! Label name already exists. Error in line {lineNo}")
            
            if name in StoredRegisters.keys() :
                raise Exception(f"Illegal naming of label! Can not use register names. Error in line lineNo{lineNo}")

            labels[name] = convertToBin(lineNo, 8)
            inst = inst[1:]
            instructions.append(inst)
            
            lineNo += 1
            break


# handling variables
        if inst[0] == "var" and varDef == False :

            if len(inst) > 2 :
                raise Exception("Illegal Variable Naming! Error in line {lineNo}")
            
            if inst[1] in StoredVars.keys():
                raise Exception(f"Illegal naming of label! Variable name already exists. Error in line {lineNo}")

            if inst[1] in StoredRegisters.keys() :
                raise Exception(f"Illegal naming of label! Variable name cannot be registers. Error in line {lineNo}")

            StoredVars[inst[1]] = "0"
            break


# handling instructions
        if inst[0] in opcodes.keys():

            instructions.append(inst)
            lineNo += 1
            break


# handling exceptions
        else :
            raise Exception(f"Illegal Syntax! Error in line {lineNo}")

n = len(StoredVars)
x = 1

for key in StoredVars.keys() :
    key = convertToBin(lineNo + x, 8)
    x += 1

lines = n + lineNo
if lines > 255:
    raise Exception(f"Memory Overload!")

if "hlt" not in instructions[-1]:
    raise Exception("Mising or Improper use of Hlt")

for i in range(lines) :

    ins= instructions[i]
    Op = ins[0]

    if (
        Op == "add" or
        Op == "sub" or
        Op == "mul" or
        Op == "xor" or
        Op == "or" or
        Op == "and" ):

        result.append(typeA(ins, i + n))

    elif Op == "mov":

        if "$" in i[-1]:
            result.append(typeB(ins, i + n))

        else:
            result.append(typeC(ins, i + n))

    elif (Op == "rs" or Op == "ls") :
        result.append(typeB(ins, i + n))

    elif (Op == "div" or Op == "not" or Op == "cmp") :
        result.append(typeC(ins, i + n))

    elif (Op == "ld" or Op == "st") :
        result.append(typeD(ins, i + n))

    elif (Op == "jmp" or Op == "jlt" or Op == "jgt" or Op == "je"):
        result.append(typeE(ins, i + n))

    elif Op == "hlt" :
        result.append(typeF())

    else:
        raise Exception("Invalid Operation Code! Error in line {line}")

for i in result :
    print(i)