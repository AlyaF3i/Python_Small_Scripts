"""eqx='(22-(2*y)+z)/4'
eqy='(1+x+(3*z))/6'
eqz='(16-(2*x)+(5*y))/8'"""
eqx='(2*y+2*z-14)/6'
eqy='(4*x+4*z-6)/10'
eqz='(11-2*x+y)/4'
temp=[1,1,1]
x,y,z=temp
html=open(r'Q1.htm','w')
html.write("""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,td,th{
                border: 3px double black;
                border-collapse: collapse;
                font-size: 0.5in;
                text-align: center;
            }
        </style>
        <title>Numerical.Quiz2.Q1</title>
    </head>
    <body>
        <table>
            <tr>
                <th>P<sub>k</sub></th><th>X</th><th>Y</th><th>Z</th>
            </tr>""")
for a in range(5):
    html.write('<tr>')
    temp[0]=eval(eqx)
    temp[1]=eval(eqy)
    temp[2]=eval(eqz)
    html.write(f'<th>P<sub>{a}</sub></th><td>{x}</td><td>{y}</td><td>{z}</td>')
    x,y,z=temp
    html.write('</tr>')
html.write("""</table>
    </body>
</html>""")
html.close()