def func(Pk,Pkk):
    #P0=1.7   P1=1.67
    #F(x)=x^2-x-3
    #Pk+1=Pk-(f(Pl)(Pk-Pkk)/(f(Pk)-f(pk-1))
    num=Pk-(Pk**2-Pk-3)*(Pk-Pkk)/(Pk**2-Pkk**2-Pk+Pkk)
    print(num)
    return num
P0=1.7
P1=1.67
temp=0
for a in range(10):
    temp=P1
    p1=func(P1,P0)
    P0=temp