import matplotlib.pyplot as draw
f = open('input.txt', 'r')
labels=['Q1', 'Q2', 'A1', 'A2', 'Mid.1', 'Mid.2','Mid.3', 'FullMark']
marks = [[] for a in range(8)]
for a in f.readlines():
    a=a[10:]
    marks[-1].append(int(a[-3:-1]))
    for ind in range(7):
        i=0
        temp=""
        while a[i]!='	':
            temp+=a[i]
            i+=1
        else:
            marks[ind].append(float(temp))
            a=a[i+1:]

for a in range(8):
    draw.subplot(2,4,a+1)
    draw.hist(marks[a],20,stacked=True,facecolor='blue', alpha=0.5,edgecolor="black")
    draw.title(f'{labels[a]}')
draw.show()