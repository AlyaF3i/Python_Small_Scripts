<?php
include('db.php');
if($output=mysqli_query($connection,"SELECT ID,Name,Q1,Q2,Assignment,Midterm,Final FROM Students;")){
    echo "<table><tr><th>ID</th><th>Name</th><th>Q1</th><th>Q2</th><th>Assignment</th><th>Midterm</th><th>Final</th></tr>";
    while($record=$mysqli_fetch_associ($output)){
        echo "<tr>";
        foreach($record as $ind->$val){
            echo "<td>".$val."</td>";
        }
        $grade=$record['Q1']+$record['Q2']+$record['Assignment']+$record['Midterm']+$record['Final'];
        echo "<td>".$grade."</td>";
        echo "</tr>";
    }
    echo "</table>"
}
?>