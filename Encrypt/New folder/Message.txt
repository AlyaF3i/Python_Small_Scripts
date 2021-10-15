from KeyGenerating import SDESKeyGenerationg as KeyGenerate
M='11011001'
key='10100010'
def XOR(num1,num2):
    # 1+1 =0, 0+0=0 1+0=1
    output=""
    for a,b in zip(num1,num2):
        if a==b:
            output+="0"
        else:
            output+="1"
    return output
def IP(num):
    output=""
    Ip=[2,6,3,1,4,8,5,7]
    for p in Ip:
        output+=num[p-1]
    return output
def IPinv(num):
    invIP=[4,1,3,5,7,2,8,6]
    output=""
    for i in invIP:
        output+=num[i-1]
    return output
def makeIt4(num):
    if len(num)==4:
        return num
    while len(num)!=4:
        num="0"+num
    return num
def S0(num):
    n1=int(num[0]+num[3],2)
    n2=int(num[1:3],2)
    S=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    return makeIt4(bin(S[n1][n2])[2:])

    if len(num)==4:
        return num
    while len(num)!=4:
        num="0"+num
    return num
def S1(num):
    n1=int(num[0]+num[3],2)
    n2=int(num[1:3],2)
    S=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    return makeIt4(bin(S[n1][n2])[2:])
def Shrink(num):
    return S0(num[0:4])+S1(num[4:])
def EP(num):
    output=""
    Ep=[4,1,2,3,2,3,4,1]
    for e in Ep:
        output+=num[e-1]
    return output

def help_SDES(Message, Key):
    PM=IP(Message)
    L0=PM[0:4]
    R0=PM[4:]
    L1=R0
    R1=XOR(XOR(L0,Shrink(XOR(EP(R0),Key))),R0)
    newM=R1+L1
    return IPinv(newM)
def SDES(Message, Keys):
    temp=help_SDES(Message,Keys[0])
    temp=help_SDES(temp, Keys[1])
    return temp
def enc(Message,key):
    keys=KeyGenerate(key)
    return SDES(Message,keys)
