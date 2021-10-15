import math
def giveIndex(num):
    num=int(num)
    if num==9:
        return 0
    elif num==11:
        return 1
    elif num==12:
        return 2
    elif num==14:
        return 3
    elif num==15:
        return 4
    elif num==17:
        return 5
    elif num==18:
        return 6
    print("there is something wrong")
    
time=["9:30-11:00 Sun/Tue","11:00-12:30 Sun/Tue","12:30-14:00 Sun/Tue","14:00-15:30 Sun/Tue","15:30-17:00 Sun/Tue","17:00-18:30 Sun/Tue","18:30-20:00 Sun/Tue","9:30-11:00 Mon/Wed","11:00-12:30 Mon/Wed","12:30-14:00 Mon/Wed","14:00-15:30 Mon/Wed","15:30-17:00 Mon/Wed","17:00-18:30 Mon/Wed","18:30-20:00 Mon/Wed"]        
file=open("classes.txt")
classes=list()
for line in file:
    classes.append((line[:2], line[3:4]))
SundayClasses=list()
MondayClasses=list()
for a,b in classes:
    if b=='s':
        SundayClasses.append(a)
    else:
        MondayClasses.append(a)
SundayClasses.sort()
MondayClasses.sort()
Class=list()
for a in range(14):
    Class.append(0)
for sun in SundayClasses:
    Class[giveIndex(sun)]+=1
for mon in SundayClasses:
    Class[giveIndex(mon)+7]+=1
for num,t in zip(Class,time):
    if num==0:
        print(t)
    
        

