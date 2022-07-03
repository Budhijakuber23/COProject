#converting binary strings to decimal

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

def conToBin(num, bits):
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

def decToBinary(n):
    x=bin(n)
    x=x.replace("0b", "")

    ans=int(x)
    return x