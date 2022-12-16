<?php
// Connect.php

$host = "localhost";
$dbs = "bysonicg_misimu";
$user = "root";
$pwd = "qRuF4e5MLqxyQc";

$conn = mysqli_connect($host, $user, $pwd, $dbs);
if (!$conn) {
    die("Error: Could not connect. " . mysqli_connect_error());
}
?>