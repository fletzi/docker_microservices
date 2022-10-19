<html>
<body>
<h1>Part stock</h1>
<?php

$s_servername = "localhost";
$s_database = "carles_database";
$s_username = "python";
$s_password = "blog.carlesmateo.com-db-password";


// Create connection
$conn = new mysql($s_servername, $s_username, $s_password, $s_database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
# echo "Connected successfully";

$s_sql = "SELECT * FROM part_stock";

$result = $conn->query($s_sql);

if ($result->num_rows > 0) {
?><table>
    <tr><th>Id Part</th><th>Part Name</th><th>Part Amount</th></tr>

<?php
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row["i_id_part"]. "</td><td>" . $row["s_part_name"]. "</td><td>" . $row["i_part_amount"]. "</td>";
        echo "</tr>";
    } ?></table><?php
} else {
    echo "<p>0 results</p>";
}
$conn->close();
?></body>
</html>