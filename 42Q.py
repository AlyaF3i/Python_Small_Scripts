""" def getNumber(num):
    output=[int(a) for a in num]
    length=len(num)
    for i in range(2,length):
        for j in range(length+1-i):
            output.append(int(num[j:j+i]))
    output.append(int(num))
    return output """

def number(num,targ,which,leng,ind=1):
    if ind==leng:
        return []
    output=list()
    for i in reversed(range(ind,which-1,ind)):
        for op in ['+','*','-']:
            st=num[0:i]+op+num[i:]
            print(st)
            if targ==eval(st):
                output.append(st)
            for j in range(ind+1,which):
                output+=number(st,targ,which-ind,leng,j)
    return output

    


a="232"
print(number(a,8,len(a),len(a)))
#print(getNumber("1234"))
