#fp=lambda x: eval('x**3-3*x-2')
#fp_Prime=lambda x: eval('3*x**2-3')
equation='x**2-x-3'
f=lambda x: eval(equation)
def Secant(x,y):
    print(f"{y}-((f({y})*({y}-{x}))\t/\t(f({x})-f({x})) ")
    eq=eval('round(y-((f(y)*(y-x))/(f(y)-f(x))),6)')
    
    return [y,eq]




equation='x**2-x-3'
p0=1.7 
p1=1.67
#Newton=lambda x: eval('(2/3)*(x**3+1)/((x**2-1))') #lambda x: x-(fp(x))/(fp_Prime(x))
for a in range(2,9):
    p0,p1=Secant(p0,p1)
    print(f"P{a}= {p1} ")