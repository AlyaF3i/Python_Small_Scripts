f=open('temp.html','w')
f.write("""
<!DOCTYPE HTML>
<html>
<head>
<style>
        table,th,td {font-size:30px;border:3px solid black;border-collapse: collapse;}
</style>
</head>
<body>
""")
#FIFO
frame=3
requests=[7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 1, 2, 0]
output=[]
WhoIsIn=[-a for a in range(1,1+frame)]
FaultOrHead=[]
currValue=[-a for a in range(1,1+frame)]
for request in requests:
    if request in WhoIsIn:
        FaultOrHead.append('H')
        output.append(currValue.copy())
        continue
    currValue[currValue.index(WhoIsIn[0])]=request
    WhoIsIn.append(request)
    WhoIsIn.pop(0)
    output.append(currValue.copy())
    FaultOrHead.append('F')
f.write("<table><tr>")
for a in requests:
    f.write(f"<th>{a}</th>")
f.write("</tr>")
for a in range(frame):
    f.write("<tr>")
    for b in range(len(requests)):
        if output[b][a]<0:
            f.write("<td>X</td>")
        else:
            f.write(f"<td>{output[b][a]}</td>")
    f.write("</tr>")
f.write("<tr>")
for a in FaultOrHead:
    f.write(f"<th>{a}</th>")
f.write("""
</tr>
</table>
</body>
</html>
""")
f.close()
