import matplotlib.pyplot as draw
def sum2Array(a,b):
    sum=0
    for c,d in zip(a,b):
        sum+=(int(c)*d)
    return sum
label=[str(n) for n in range(21)]
Marks=[0*n for n in range(21)]
with open(r'PsychoMarks.txt','r') as f:
    for line in f:
        if len(line)>6:
            continue
        Marks[int(line[:2])]+=1
Sum=sum2Array(label,Marks)
draw.bar(label,Marks)
draw.grid()
draw.show()