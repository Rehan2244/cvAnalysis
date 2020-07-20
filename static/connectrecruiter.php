<?php
$server="localhost";
$db="test";
$username="root";
$pwd="";
$conn=mysqli_connect($server,$username,$pwd,$db);
$recentered=$_GET["recEntered"];
echo $recentered;
if(!$conn)
{
    die("connection failed".$conn->connect_error);
}
$selectcmd="select * from recruiterLogin";
$result=mysqli_query($conn,$selectcmd);
if(mysqli_num_rows($result)>0)
{
    while($row=$result->fetch_assoc())
    {
        if($row["username"]==$_GET["recEntered"] && $row["password"]==$_GET["recPwd"])
        {
            header("Location:analysis.html");
        }
        else{
        echo "<script> alert('Enter Valid Details'); window.location='/recruiterloginpage.html';</script>";
        //header("Location:recruiterloginpage.html");
        }
    }

}

?>