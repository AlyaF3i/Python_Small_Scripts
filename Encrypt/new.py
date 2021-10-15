#p=input('Input 10 bits')
#p10=[3,5,2,7,4,10,1,9,8,6]
def P10(num):
    p10=[3,5,2,7,4,10,1,9,8,6]
    output=""
    for a in p10:
        output+=num[a-1]
    return output
def shiftLeft(num):
    l=num[0:5]
    r=num[5:]
    l=l[1:]+l[0]
    r=r[1:]+r[0]
    return l+r
def P8(num):
    p8=[6,3,7,4,8,5,10,9]
    output=""
    for a in p8:
        output+=num[a-1]
    return output
def SDESKeyGenerationg(p10):
    Kp=P10(p10)
    #circular shift left
    Kp1=shiftLeft(Kp)
    Kp2=shiftLeft(shiftLeft(Kp1))
    k1=P8(Kp1)
    k2=P8(Kp2)
    return list([k1,k2])
#print(shiftLeft(shiftLeft('1000001100')))
#print(SDESKeyGenerationg('1010000010'))









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

def S0(num):
    n1=int(num[0]+num[3],2)
    n2=int(num[1:3],2)
    S=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    return bin(S[n1][n2])[2:].zfill(2)
def S1(num):
    n1=int(num[0]+num[3],2)
    n2=int(num[1:3],2)
    S=[
        [0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]
    ]
    return bin(S[n1][n2])[2:].zfill(2)
def Shrink(num):
    temp=str(   S0( num[0:4]    )+  S1( num[4:]    )    )
    return temp[1]+temp[3]+temp[2]+temp[0]
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
    R1=XOR( L0  ,   Shrink( XOR(    EP(R0)  ,   Key )  )  )
    temp=L1+R1
    return temp
def help_SDES1(Message, Key):
    L0=Message[0:4]
    R0=Message[4:]
    L1=R0
    R1=XOR(L0,Shrink(XOR(EP(R0),Key)))
    return IPinv(R1+L1)
def SDES(Message, Keys):
    temp=help_SDES(Message,Keys[0])
    temp=help_SDES1(temp, Keys[1])
    return temp
def enc(Message,key):
    keys=KeyGenerate(key)
    return SDES(Message,keys)








import tkinter as tk
from Message import enc
from tkinter import *
window = tk.Tk()
window.title("S-Des Encryption")
def run():
    Data1=Enter1.get()
    Data2=Enter2.get()
    label33['text']=f"{enc(Data1,Data2)}"

label1=tk.Label(window, text="Plain text: ").grid(row=0,column=0)
Enter1=tk.Entry(window, bd =5)
Enter1.grid(row=0,column=1)
#Data1=Enter1.get()
label2=tk.Label(window, text="Key: ").grid(row=2,column=0)
Enter2=tk.Entry(window, bd =5)
Enter2.grid(row=2,column=1)
8 / 2
#Data2=Enter2.get()
label331=tk.Label(window, text="the Output: ")
label331.grid(row=4,column=0)
label33=tk.Label(window, text="")
label33.grid(row=4,column=1)
Data3=Enter1.get()
#############
label3=tk.Label(window, text="Plain text").grid(row=6,column=0)
Enter3=tk.Entry(window, bd =5)
Enter3.grid(row=6,column=1)
Data3=Enter1.get()
label4=tk.Label(window, text="Decrypt").grid(row=8,column=0)
Enter4=tk.Entry(window, bd =5)
Enter4.grid(row=8,column=1)
button=Button(window, text="Encrypt", command=run)
button.grid(row=9,column=0)
Data4=Enter2.get()
window.mainloop()