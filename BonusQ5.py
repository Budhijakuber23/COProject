import math

dict = {
    "M":20,
    "K":10, 
    "G":30, 
    "T":40
}
print("==="* 20)
print()
print(" "*22 + "BONUS QUESTION" + " "*24)
print()
print("==="* 20)
print()
s, b = input("Enter the space in Memory: ").split()
s = int(s)

if b[1] == "B":
    space = s.bit_length() -1 + dict[b[0]]
if b[1] == "b":
    temp = (s*(2**dict[b[0]]))//8
    space = temp.bit_length() - 1 


print("How do you want your memory to be addressed: ")
print()
print("1. Bit Addressable Memory\n2. Nibble Addressable Memory\n3. Byte Addressable Memory\n4. Word Addressable Memory")
n = int(input("Enter your choice: "))
if n == 1:
    p = space + 3

elif n == 2:
    p = space + 1

elif n == 3:
    p = space

elif n == 4:
    # assuming word to be of 16 bits
    word = int(input("Enter no. of words: "))
    bytes = word//8
    gg = math.log(bytes, 2)
    p = int(space - gg)
print()
print("Query Types\n1. ISA and Instructions\n2. System Enhancement")
x = int(input("Enter Query:"))
print()

if (x == 1) :

    ins_bits = int(input("Enter the length of one instruction in bits: "))
    reg_bits = int(input("Enter the lenth of register in bits: "))

    q = ins_bits - p - reg_bits
    r = ins_bits - q - (2*reg_bits)
    max_ins = 2**q
    max_reg = 2**reg_bits

    print()
    print(f"Minimum bits to represent address: {p}")
    print(f"No. of bits needed by opcode: {q}")
    print(f"No. of filler bits: {r}")
    print(f"Maximum no. of instructions supported by ISA: {max_ins}")
    print(f"Maximum no. of registers supported by this ISA: {max_reg}")

elif (x==2) :

    y = int(input("Enter Type (1/2): "))
    word = int(input("Enter the no. of CPU bits: "))
    if (y == 1):
        print()
        print("1. Bit Addressable Memory\n2. Nibble Addressable Memory\n3. Byte Addressable Memory\n4. Word Addressable Memory")
        z = int(input("Enter your choice: "))
        print()
        while(z==n):
            print("Machine is in that addressable memory! Please choose again")
            z = int(input("Enter your choice: "))

        if (z == 1):
            pins = space + 3
        elif (z == 2):
            pins = space + 1
        elif (z == 3):
            pins = space
        elif (z == 4):
            bytes = word//8
            gg = math.log(bytes, 2)
            pins = int(space - gg)
        if pins > p:
            print(f"Answer: +{pins-p}")
        elif pins < p:
            print(f"Answer: -{p-pins}")
    elif (y==2):
        apins = int(input("Enter the no. of memory pins: "))
        print("1. Bit Addressable Memory\n2. Nibble Addressable Memory\n3. Byte Addressable Memory\n4. Word Addressable Memory")
        z = int(input("Enter your choice: "))
        print()
        if (z==1):
            m = apins - 3
        elif (z==2):
            m = apins -1
        elif(z==3):
            m = apins
        elif(z == 4):
            bytes = word//8
            gg = math.log(bytes, 2)
            m = int(apins + gg)
    
        if 10<=m<20 :
            a = m -10
            print(f"Answer: {2**a} KB")
        elif 20<=m<30 :
            a = m - 20
            print(f"Answer: {2**a} MB")
        elif 30<=m<40 :
            a = m - 30
            print(f"Answer: {2**a} GB")
        elif m>= 40 :
            a = m - 40
            print(f"Answer: {2**a} TB")