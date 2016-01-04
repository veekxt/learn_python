<?php
$dbm = new PDO('mysql:host=localhost;dbname=mysql','root','');
$statement = $dbm->query("SELECT User AS _message FROM user");
$row = $statement->fetch(PDO::FETCH_ASSOC);
echo htmlentities($row['_message']);
