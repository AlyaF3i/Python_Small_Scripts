way=[""]
def allWays(arr, index,wayIndex):
    global way
    if len(arr)==index:
        return None
    if len(arr)-1==index:
        way[wayIndex]+=chr(64+int(arr[index]))
    else:
        if int(arr[index])>2 and int(arr[index+1])<7:
            way[wayIndex]+=chr(64+int(arr[index]))
            allWays(arr, index+1, wayIndex)
        else:
            temp=way[wayIndex]
            way[wayIndex]+=chr(64+int(arr[index]))
            allWays(arr, index+1,wayIndex)
            way.append(temp)
            tempIndex=len(way)-1
            way[tempIndex]+=chr(64+int(arr[index]+arr[index+1]))
            allWays(arr, index+2, tempIndex)
num=input()
digts=[a for a in num]
allWays(digts, 0, 0)
for EachOne in way:
    print(EachOne)
