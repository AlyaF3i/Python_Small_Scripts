

How=int(input(""))
up=1
down=1
arr=[]
for a in range(How):
    a= str(input("")).split(" ")
    up*=int(a[0])
    down*=int(a[1])
    arr.append(int(a[0]))
a=min(up,down)
while a!=1:
    if up%a==0 and down%a==0:
        up/=a
        down/=a
        a=min(up,down)
    a-=1
    up=int(up)
    down=int(down)
print(f"{up} {down}")