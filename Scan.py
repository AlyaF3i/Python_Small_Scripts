def scan(arr):
    sum=0
    output=[]
    for index in range(len(arr)-1):
        output.append(abs(arr[index]-arr[index+1]))
        sum+=abs(arr[index]-arr[index+1])
    return [sum,output]
sc=[50,34,11,0,62,64,95,119,123,180]
look=[50,34,11,62,64,95,119,123,180]
print(f"Scan: {scan(sc)[0]/8}")
print(f"look: {scan(look)[0]/8}")