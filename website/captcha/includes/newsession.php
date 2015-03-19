<?php
session_start();
require '../includes/rand.php';
$randomObj = new RandomGen();
$str = $randomObj->createRandom();


$_SESSION['captcha_id'] = $str;

?>
