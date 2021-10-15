#fp=lambda x: eval('x**3-3*x-2')
#fp_Prime=lambda x: eval('3*x**2-3')
x=2.1
Newton=lambda x: eval('(2/3)*(x**3+1)/((x**2-1))') #lambda x: x-(fp(x))/(fp_Prime(x))
for a in range(5):
    fp=round(Newton(x),6)
    print(f"P{a}= {x},\t f(P{a})= {fp}")
    x=fp