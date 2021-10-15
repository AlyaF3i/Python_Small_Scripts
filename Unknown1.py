f = open('report.html', 'w')

code = """

<html>

<head>
<title>My chat analysis report</title>
</head>
<body>
<h1 align="center"style="color:#4682B4"> Data Analysis Report </h1>
<h2 style="color:#4682B4">Group Messages Data </h2>
<table border = "1">
<tr><th>Names</th></tr>
<tr><td>Texts</td></tr>"
</table>
<img src='plot_1.png'>

<br>

<table border='1'>
<tr>
<th>Date</th>
<th>Texts</th>
</tr>
<tr>
<th></th>
<th></th>
</tr>

<img style ='margin-left:10px;'src='plot_2.png'>


</body>
</html>
"""

f.write(code)
f.close()