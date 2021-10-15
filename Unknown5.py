import matplotlib.pyplot as draw
Ns=range(100)
iteration=0
iterations=[]
for N in Ns:
    for a in range(2,N//2):
        if N%a==0:
            for b in range(2,N//(a*2)):
                iteration+=1
                if N%(a*b)==0:
                    c=N//(a*b)
                    #print(f"{a}, {b}, {c}")

    iterations.append(iteration)
    iteration=0
draw.plot(Ns,iterations)
draw.show()
                