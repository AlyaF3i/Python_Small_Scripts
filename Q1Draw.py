import matplotlib.pyplot as draw
import numpy as num

equation='x**3-30*x**2+2552'
xaxis= num.linspace(0, 20, 100)
yaxis=num.linspace(0, 20, 100)
a=lambda x : eval(equation)
yaxis= [a(x) for x in yaxis]
draw.xlabel("x")
draw.ylabel("f(x)")
draw.plot(xaxis,yaxis)
draw.show()
