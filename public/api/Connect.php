<?php
// Connect.php

$host = "localhost";
$dbs = "bysonicg_misimu";
$user = "bysonicg";
$pwd = "MarvelDc123";

$conn = mysqli_connect($host, $user, $pwd, $dbs);
if (!$conn) {
    die("Error: Could not connect. " . mysqli_connect_error());
}
?>