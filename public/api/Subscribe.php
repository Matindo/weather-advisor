<?php
// Subscribe.php

include("Connect.php");

$result = array('error'=>false);
$action = '';

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    if ($action == 'addRegular') {
        $fname = $_POST['fname'];
        $lname = $_POST['lname'];
        $email = $_POST['email'];
        $whatsapp = $_POST['whatsapp'];
        $telegram = $_POST['telegram'];
        $phone = $_POST['phone'];
        $location = $_POST['location'];
        $pass = crypt($_POST['pword'], '$6$rounds=427$CraZyMommAkateNinYasI$');
        
        $sql = $conn->query("INSERT INTO regular(fname, lname, email, phone, whatsapp, telegram, location, pwd) VALUES ('$fname', '$lname', '$email', '$phone', '$whatsapp', '$telegram', '$location', '$pass')");
        if($sql){
            $result['message'] = "New subscriber $fname added successfully!";
        } else {
            $result['error'] = true;
            $result['message'] = "Failed to subscribe: " . $conn->error;
        }
    }
}

$conn->close();
echo json_encode($result);
?>