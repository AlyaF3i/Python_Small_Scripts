from math import ceil,log,cos
def bisection(a,b,c):
    #equation='x**3-30*x**2+2552' # here you write the equation
    equation='cos(x)+1-x'
    x=a
    fa=round(eval(equation),6)
    x=b
    fb=round(eval(equation),6)
    x=c
    fc=round(eval(equation),6)
    #print(f"f(a)= {fa},\t f(b)= {fb},\t f(c)= {fc}")
    if fc==0:
        print("solved c= {c}")
        return [0,0]
    if (fc<0 and fb>0) or (fc>0 and fb<0):
        return [c,b]
    else :
        return [a,c]
# here you wriwte the range
a,b=[1,2]
iterations=ceil((log(b-a)-log(10**(-8)))/log(2))
#print(iterations)
for iteration in range(iterations):
    #print(f"iteration number {iteration}")
    c=round((a+b)/2,6)
    #print(f"a= {a},\t b= {b},\t c= {c}")
    a,b=bisection(a,b,c)
    if a+b==0:
        break
else:
    print(f"iteration number {iteration}")
    print(f"a= {a},\t b= {b},\t c= {c}")
