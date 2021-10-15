a=0.1 #غراب
c=5 # حمام
# j صقر
for i in range(10,101,10):
    for j in range(1,101-i):
        for k in range(1,101-i-j):
            answer= (i*a)+j+(k*c)
            if answer == 100 and i+j+k==100:
                print(f"7mam: {k}, 3*rab: {i}, 98r: {j}")