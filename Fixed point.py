from math import cosh
err=lambda y,x: round(eval('abs(y-x)'),6)
p0=2.2
x=p0
equation='1+(2/x)'
error='-'
fp=round(eval(equation),6)
for a in range(6):
    temp=fp
    fp=round(eval(equation),6)
    print(f"P{a}= {x},\t f(P{a})= {fp},\t error: {error}")
    x=round(eval(equation),6)
    error=err(temp,x)
print(f"P3= {x},\t f(P3)= {fp},\t error: {error}")
