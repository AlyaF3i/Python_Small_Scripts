previous=[0,0,0]
x,y,z=previous
eqx='(10+2*y+3*z)/6'
eqy='(9+x-4*z)/6'
eqz='(-22-3*x-2*y)/10'
tol=1e-08
iteration=0
checkTolrance=lambda num: abs(num)<tol
while True:
    x,y,z=previous
    previous[0]=eval(eqx)
    previous[1]=eval(eqy)
    previous[2]=eval(eqz)
    iteration+=1
    if checkTolrance(x-previous[0]) or checkTolrance(y-previous[1]) or checkTolrance(z-previous[2]):
        break
print(f"x={x}, y={y}, z={z}, k={iteration}")