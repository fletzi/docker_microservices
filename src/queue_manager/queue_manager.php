<html>
<body>
<h1>Car queue</h1>
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

$s_sql = "SELECT * FROM car_queue";

$result = $conn->query($s_sql);

if ($result->num_rows > 0) {
?><table>
    <tr><th>Id Car</th><th>Model Code</th><th>Color Code</th><th>Extras</th><th>Right Side</th><th>City to ship</th></tr>

<?php
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . $row["i_id_car"]. "</td><td>" . $row["s_model_code"]. "</td><td>" . $row["s_color_code"]. "</td>";
        echo "<td>" . $row["s_extras"] . "</td><td>" . $row["i_right_side"] . "</td><td>" . $row["s_city_to_ship"] . "</td>";
        echo "</tr>";
    } ?></table><?php
} else {
    echo "<p>0 results</p>";
}
$conn->close();
?></body>
</html>