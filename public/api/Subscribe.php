<?php
// Subscribe.php

include("Connect.php");

$result = array('error'=>false);
$action = '';
$message = '';

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    if ($action == 'addRegular') {
        $fname = $_POST['fname'];
        $lname = $_POST['lname'];
        $email = $_POST['email'];
        $telegram = $_POST['getTelegram'];
        $phone = $_POST['phone'];
        $location = $_POST['location'];
        $pass = crypt($_POST['pword'], '$6$rounds=427$CraZyMommAkateNinYasI$');
        
        $sql = $conn->query("INSERT INTO regular(fname, lname, email, phone, telegram, location, password) VALUES ('$fname', '$lname', '$email', '$phone', '$telegram', '$location', '$pass')");
        if($sql){
            $result['message'] = "New subscriber $fname added successfully!";
            if ($telegram == 'yes') {
                mail($email, 'Telegram link To Our Bot', $message);
            }
        } else {
            $result['error'] = true;
            $result['message'] = "Failed to subscribe: " . $conn->error;
        }
    }
    
    if ($action == 'addFarmer') {
        $fname = $_POST['fname'];
        $lname = $_POST['lname'];
        $email = $_POST['email'];
        $telegram = $_POST['getTelegram'];
        $phone = $_POST['phone'];
        $location = $_POST['location'];
        $pass = crypt($_POST['pword'], '$6$rounds=427$CraZyMommAkateNinYasI$');
        
        $sql = $conn->query("INSERT INTO farmer(fname, lname, email, phone, telegram, location, password) VALUES ('$fname', '$lname', '$email', '$phone', '$telegram', '$location', '$pass')");
        if($sql){
            $result['message'] = "New farmer $fname added successfully!";
            if ($telegram == 'yes') {
                mail($email, 'Telegram link To Our Bot', $message);
            }
        } else {
            $result['error'] = true;
            $result['message'] = "Failed to register: " . $conn->error;
        }
    }
    
    if ($action == 'addOrganization') {
        $orgname = $_POST['oname'];
        $email = $_POST['email'];
        $phone = $_POST['phone'];
        $location = $_POST['location'];
        $pass = crypt($_POST['pword'], '$6$rounds=427$CraZyMommAkateNinYasI$');
        
        $sql = $conn->query("INSERT INTO organization(oname, email, phone, location, password) VALUES ('$orgname', '$email', '$phone', '$location', '$pass')");
        if($sql){
            $result['message'] = "New organization $orgname added successfully!";
            mail($email, 'Telegram link To Our Bot', $message);
        } else {
            $result['error'] = true;
            $result['message'] = "Failed to register: " . $conn->error;
        }
    }
    
    if ($action == 'login') {
    $email = mysqli_real_escape_string($conn, $_POST['email']);
    $pass = crypt(mysqli_real_escape_string($conn, $_POST['pword']), '$6$rounds=427$CraZyMommAkateNinYasI$');
    $table = 'regular';
    $sql = $conn->query("SELECT * FROM regular WHERE email='$email'");
    if ($sql->num_rows = 0) {
        $sql = $conn->query("SELECT * FROM farmer WHERE email='$email'");
        $table = 'farmer';
    }
    if ($sql->num_rows = 0) {
        $sql = $conn->query("SELECT * FROM organization WHERE email='$email'");
        $table = 'organization';
    }
    if($sql->num_rows > 0){
        while($row = $sql->fetch_assoc()){
            if($row['password'] == $pass){
                if (($table == 'regular') || ($table == 'farmer')) {
                    $result['user'] = array('id'=>$row['id'], 'firstName'=>$row['fname'], 'lastName'=>$row['lname'], 'email'=>$row['email'], 'phone'=>$row['phone'], 'location'=>$row['location']);
                } else {
                    $result['user'] = array('id'=>$row['id'], 'orgName'=>$row['oname'],  'email'=>$row['email'], 'phone'=>$row['phone'], 'location'=>$row['location']);
                }
                $result['message'] = "Successful login. Welcome back, ".$row['firstName'];
            } else {
                $result['error'] = true;
                $result['message'] = "Invalid password!";
            }
        }
    } else {
        $result['error'] = true;
        $result['message'] = "No such email address exists in our records!";
    }
  }
}

$conn->close();
echo json_encode($result);
?>