def L(a):
    if a==0:
        return "F"
    elif a==1:
        return "D"
    elif a==1.5:
        return "D+"
    elif a==2:
        return "C"
    elif a==2.5:    
        return "C+"
    elif a==3:
        return "B"
    elif a==3.5:
        return "B+"
    else:
        return "A"
file=open("AllPossiblity.txt", 'w')
marks=[0]+[a/2 for a in range(2,9)]
for a in marks:
    for b in marks:
        for c in marks:
            for d in marks:
                for f in marks:
                    for g in marks:
                        for h in marks:
                            ee=(a*3+b*3+c*3+d*3+f*3+g*3+(h*2))/20
                            if ee<2.94 and ee>2.92 and h==0:
                                print(f"{L(a)}, {L(b)}, {L(c)}, {L(d)}, {L(f)}, {L(g)}, {L(h)} -> {ee}\n")

file.close()
            



                