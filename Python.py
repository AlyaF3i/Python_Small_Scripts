def printarr(arr):
    for a in arr:
        print(a)
twoDarr=[ [0 for a in range(4)] for b in range(4)]
def change(num):
    global twoDarr
    for a in range(4):
        twoDarr[num][a]=1
    for a in range(4):
        twoDarr[a][num]=0

arr=[0,1,2,3,0,1,2,3]
#twoDarr=[ [0 for a in range(4)] for b in range(4)]
for a in arr:
    change(a)
    printarr(twoDarr)
    print("_______")