dic = {"M":10,"O":20,"H":30,D:40}
table = /
"""
<table>
    <tr>
        <th> Name </th>
        <th> Message Count </th>
    </tr>
"""
for key,val in dic:
    table+= /
    f"""
        <tr>
            <td> {key} </td>
            <td> {val} </td>
        </tr>
    """
table+="</table>"
