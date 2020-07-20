<?php
$server="localhost";
$db="test";
$username="root";
$pwd="";
$conn=mysqli_connect($server,$username,$pwd,$db);
$userentered=$_GET["userEntered"];
echo $userentered;
if(!$conn)
{
    die("connection failed".$conn->connect_error);
}
$selectcmd="select * from userLogin";
$result=mysqli_query($conn,$selectcmd);
if(mysqli_num_rows($result)>0)
{
    while($row=$result->fetch_assoc())
    {
        if($row["username"]==$_GET["userEntered"] && $row["password"]==$_GET["userPwd"])
        {
            header("Location:uploadfile.html");
        }
        else{
        echo "<script> alert('Enter Valid Details'); window.location='/login.html';</script>";
        //header("Location:recruiterloginpage.html");
        }
    }

}

?>