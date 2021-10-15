from math import ceil,log
def bisection(a,b,c):
    equation='x**3-30*x**2+2552'
    x=a
    fa=round(eval(equation),6)
    x=b
    fb=round(eval(equation),6)
    x=c
    fc=round(eval(equation),6)
    print(f"<tr><td>f(a)</td><td> {fa}</td><td> f(b)</td><td> {fb}</td><td> f(c)</td><td> {fc}</td></tr>")
    if fc==0:
        print("solved c= {c}")
        return [0,0]
    if (fc<0 and fb>0) or (fc>0 and fb<0):
        return [c,b]
    else :
        return [a,c]

a=0
b=20
iterations=ceil((log(b-a)-log(10**(-8)))/log(2))
print("<!DOCTYPE html>\n<html lang=\"en\">\n\t<head>\n\t\t<title>Assignment 1 Q1</title>\n\t<style>\ntable,tr,td {border: {1px solid black;}\t\t</style>\n\t</head>\n\t<body>")
print("<table style=\"border: 1px solid black; \">")
for iteration in range(iterations):
    print('<tr>')
    print(f"<td rowspan=\"2\">Iteration number {iteration}")
    c=round((a+b)/2,6)
    print(f"<td>a</td><td> {a}</td><td> b</td><td> {b}</td><td> c</td><td> {c}</td></td>")
    a,b=bisection(a,b,c)
    if a+b==0:
        break

print('</table></body></html>')

