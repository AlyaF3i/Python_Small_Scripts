eqx='(22-(2*y)+z)/4'
eqy='(1+x+(3*z))/6'
eqz='(16-(2*x)+(5*y))/8'
temp=[1,1,1]
x,y,z=temp
for a in range(4+1):
    temp[0]=eval(eqx)
    temp[1]=eval(eqy)
    temp[2]=eval(eqz)
    print(f'{a}\t{round(x,6)}\t{round(y,6)}\t{round(z,6)}')
    x,y,z=temp