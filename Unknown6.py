import matplotlib.pyplot as draw
Ns=range(100)
iteration=0
iterations=[]
for N in Ns:
    for a in range(2,N):
        for b in range(2,N):
            iteration+=1
            if (N/(a*b)).is_integer():
                c = N//(a*b)
    iterations.append(iteration)
    iteration=0
draw.plot(Ns,iterations)
draw.show()
                