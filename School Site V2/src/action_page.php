<?php
if(isset($_POST['submit']))
{
    $secretKey = "6Ld8IfUaAAAAADvbcOACYun-YU7w6XJTQYuknDgF";
    $responsKey = $_POST['g-recaptcha-response'];
    $UserIP = $_SERVER['REMOTE_ADDR'];
    $url = "http://www.google.com/recaptcha/api/siteverify?secret=$secretKey&response=$responsKey&remoteip=$UserIP";

    $response = file_get_contents($url);
    $response = json_decode($response);


}
?>