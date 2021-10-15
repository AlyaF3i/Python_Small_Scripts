import webbrowser
#from Dictionary import get_dict
#import dates as date
#import stats as s

f = open('report.html', 'w')

table = """
<html>

<head>
<title>My chat analysis report</title>
</head>
<body>
<h1 align="center"style="color:#4682B4"> Data Analysis Report </h1>
<h2 style="color:#4682B4">Group Messages Data </h2>
"""
dic = {"hello":1,"How":2,"Are":3,"You?":4}
table += """
<table>
    <tr>
        <th> Name </th>
        <th> Message Count </th>
    </tr>
"""
for key,val in dic.items():
    table+=f"""
        <tr>
            <td> {key} </td>
            <td> {val} </td>
        </tr>
    """
table += """
</table>
<img src='plot_1.png'>
<br>
<img style ='margin-left:10px;'src='plot_2.png'>
</body>
</html>
"""
f.write(table)
f.close()
webbrowser.open('report.html', new = 1)