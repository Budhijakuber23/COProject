#converting binary strings
def convertToDecimal(Sbin):
    num = str(Sbin)
    # print(bin_num)
    Return = 0
    n = len(num)
    for i in range(n):
        if num[n-i-1] == "1":
            Return += pow(2, i)
        else:
            continue
    return Return

#write a function to convert a number from decimal to binary 
def convertToBin(num, Bits):
    if num == 0:
        return "0" * Bits
    ans = ""
    while num > 1:
        x=str(num%2)
        ans +=x
        num = int(num / 2)
    ans = "1" + ans
    Left = Bits - len(ans)
    if Left > 0:
        y= "0" * Left
        ans = y + ans
    return ans
    

#convert a number from decimal to binary
def decimalToBinary(n):   
    sol= int(bin(n).replace("0b", ""))
    return sol