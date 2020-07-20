<?php
$server="localhost";
$db="test";
$username="root";
$pwd="";
$conn=mysqli_connect($server,$username,$pwd,$db);
$enteredusernmae=$_GET["enteredUsername"];
$enteredpassword=$_GET["enteredPassword"];
$enteredcontact=$_GET["enteredMobile"];
$enteredmail=$_GET["enteredEmail"];
if(!$conn)
{
    die("connection failed".$conn->connect_error);
}
$insertcmd="insert into userlogin(`username`,`password`,`email`,`mobile_no`) values('$enteredusernmae','$enteredpassword','$enteredmail',$enteredcontact)";
echo $insertcmd;
if(mysqli_query($conn,$insertcmd))
{
echo '<script>alert("Successfully Sign up")</script>';
}
else
{
    echo '<script>alert("Error")</script>';
}
mysqli_close($conn);
?>