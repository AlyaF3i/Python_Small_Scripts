from math import sin,cos,tan,pi,log,e,ceil
def Stringing(s):
    a=list(s.keys())
    print(a)
    string=f"a: {s[a[0]]}\tb: {s[a[1]]}\tc: {a[2]}\na: {a[0]}\tb: {a[1]}\tc: {a[2]}"
    return string
def bisection_h1(equ, a, b):
    c=(a+b)/2
    map={
        a:0,
        b:0,
        a:0
    }
    x=a
    map[a]=eval(equ)
    x=b
    map[b]=eval(equ)
    x=c 
    map[c]=eval(equ)
    if map[c]==0:
        print(f"${c} is the root")
    if map[c]<0 and map[b]<0:
        b=c
    else:
        a=c
    print(f"{a} {b} {c}")
    print(map)
    s=Stringing(map)
    print(s)
    return [a,b]
def bisection(equ, a, b,tol):
    iteration=ceil((log(b-a)-log(10**(tol)))/log(2))
    for a in range(iteration):
        a,b=bisection_h1(equ,a,b)

bisection('x**3-30*x**2+2552',0,20,-8)



    