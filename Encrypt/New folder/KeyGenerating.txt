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
def shiftLeft2(num):
    l=num[0:5]
    r=num[5:]
    l=l[2:]+l[0:2]
    r=r[2:]+r[0:2]
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