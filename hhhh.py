import csv
output=open(r"options.html", 'w')
output.write("""
<!DOCTYPE html>
<html lang="en">
<head>
<title>Reyamo</title>
<style>
div{
border-radius: 5%;
border: 3px solid black;
width:fit-content;
margin: 10px;
background-color: #F0F0F0;
box-shadow: 0 8px 16px 0 rgba(0,0,0,1);
transition: 0.3s;
padding: 10px;
}
div:hover{
background-color: #C5C5C5;
}
.wrapper{
display: flex ;
flex-wrap: wrap;
}
</style>
</head>
<body>
<section class="wrapper">
""")
hello=open(r'reyamo.csv')
myFile= list(csv.reader(hello))[1:]
for record in myFile:
    output.write(f"""<div href="{record[7]}">
<h1> Catgory: {record[0]}</h1>
<h2> Name: {record[1]}</h2>
<img src="{record[2]}" width="300" height="300">
<p> <b>Quantity:</b>{record[3]} </p>
<p> <b>Price:</b>{record[4]} </p>
<p> <b>Description: </b>{record[5]} </p>
<p> <b>Shipper: </b>{record[6]} </p>
</div>""")
output.write("""
</section>
</body>
</html>
""")
output.close()