from definations import (labels, register, opcodes, StoredRegisters, StoredVars)

from co_helper import convertToBin


def typeA (inst, line):

    result = ""

    if len(inst) != 4:
        raise Exception(f"TypeA instruction requires 3 operands! Error in line {line}")

    op = inst[0]
    Reg1 = inst[1]
    Reg2 = inst[2]
    resultReg = inst[3]

    result += opcodes[op] + "00"

    if (Reg1 not in StoredRegisters.keys()) or (Reg2 not in StoredRegisters.keys()) or (resultReg not in StoredRegisters.keys()):
        raise Exception(f"Invalid register! Error in line {line}.")

    if "FLAGS" in inst :
        raise Exception(f"FLAG register can not be used to store bits in typeA instruction! Error in line {line}.")

    result = result + register[Reg1] + register[Reg2] + register[resultReg]

    return result


def typeB(inst, line):

    result = ""

    if len(inst) != 3:
        raise Exception(f"TypeB instruction requires 2 commands! Error in line {line}")

    op = inst[0]
    reg1 = inst[1]
    value = inst[2]

    if (reg1 not in StoredRegisters.keys()):
        raise Exception(f"Invalid register! Error in line {line}.")

    result += opcodes[op] + register[reg1]

    if value[0] == "$":
        imm = int(value[1:])
        if ((imm > 255) or (imm < 0)) :
            raise Exception (f"Memory Overload! Error in line {line}")

        else :
            imm = convertToBin(imm, 8)
            result += imm
            return result

    else :
        raise Exception(f"Syntax Error! Error in line {line}")


def typeC (inst, line) :

    result = ""

    if len(inst) != 3:
        raise Exception(f"TypeC instruction requires 2 commands! Error in line {line}")

    op = inst[0]
    reg1 = inst[1]
    reg2 = inst[2]

    if (reg1 not in StoredRegisters.keys()) or (reg2 not in StoredRegisters.keys()):
        raise Exception(f"Invalid register! Error in line {line}.")

    result += opcodes[op]
    result += "00000"
    result += register[reg1] + register[reg2]

    return result

def typeD (inst, line) :

    result = ""

    if len(inst) != 3:
        raise Exception(f"TypeD instruction requires 2 commands! Error in line {line}")

    op = inst[0]
    reg1 = inst[1]
    mem = inst[2]

    if reg1 not in StoredRegisters.keys() :
        raise Exception(f"Invalid Register! Error in line {line}")

    if mem not in StoredVars.keys() :
        raise Exception(f"Undeclared variable used! Error in line {line}")

    if mem in labels.keys() :
        raise Exception(f"Label used in place of variable! Error in line {line}")

    result += opcodes[op] + register[reg1] + StoredVars[mem]
    return result

def typeE (inst, line) :

    result = ""

    if len(inst) != 2:
        raise Exception(f"TypeD instruction requires 1 command! Error in line {line}")

    op = inst[0]
    mem = inst[1]

    if mem not in labels.keys() :
        raise Exception(f"Label not declared! Error in line {line}")

    if mem in StoredVars.keys() :
        raise Exception(f"Cannot use Variables in this instruction! Error in line {line}")

    result += opcodes[op] + "000" + labels[mem]

    return result

def typeF () :

    result = "01010"
    x = "0" * 11
    result += x
    return result
