#arr=[4,6,7,3,2,5,13,77]
#arr=[150,320,553]

def MaxAndMin(arr):
    z= len(arr)
    if z==0:
        return (-1,-1)
    Max=arr[0]
    Min=arr[0]
    
    for a in arr:
        if a > Max:
            Max = a
        if a<Min:
            Min=a    
    return Max,Min    

arr=[]
print(MaxAndMin(arr))