<?php
session_start();

if(isset($_POST["logOut"])){ //logs out user if log out button pressed
    session_unset();
    session_destroy();
    header("Location: index.php");
    exit();
}
$username = $_POST["username"]; //these get all the data from the login form 
$password = $_POST["password"];

$fname = $_POST["fname"];//these get all the data from the registor form 
$lname = $_POST["lname"];
$cpassword = $_POST["cpassword"];
$display = $_POST["display"];

/*
$dbusername = "";//connects to the database 
$dbpassword = "";
$dbname = "";
$conn = mysqli_connect("localhost", $dbusername, $dbpassword, $dbname);

if (!$conn) {
    die("Connection failed: " . mysqli_connect_error()); //gives reason for connection error 
}

$logAttempt = false;
$notLogged = true;


if (isset($fname)){ //registers a new user 
    $hashPassword = password_hash($password, PASSWORD_DEFAULT);
    $sql = "INSERT INTO Users VALUES ('$username', '$fname', '$lname', '$hashPassword', $display);";
    if (mysqli_query($conn, $sql) ) {
        $notRegistered = false;
    } else {
        $notRegistered = true;
    }
}


if(isset($username)&&$notRegistered!=true){ //logs in a user 
    $logAttempt = true;
    $sql = "SELECT * FROM Users";
    $result = mysqli_query($conn,$sql);
    if (mysqli_num_rows($result) > 0) {
        while( $row = mysqli_fetch_assoc($result) ) {
            if (($row["UserName"] == $username) && (password_verify($password, $row["Password"]))){
                $_SESSION["userName"] = $username;
                $notLogged = false;
                break;
            }
        }
    }
}




mysqli_close($conn);
*/
?>
<html>
    <head>
        <link rel="stylesheet" href="SusStylesheet.css">
    </head> 
    <body>
           <div class="main">
            <?php if (isset($_SESSION["userName"])) {?>
                <div>
                    <form action="characterPage.php" method="get">
                        <h1>Welcome To Placeholder Name</h1>
                        <button>Click here to play</button>
                    </form>
                        <form action="index.php" method="post">
                        <button name="logOut">log out</button>
                    </form>
                </div>

            <?php }else{?>
                <div>
                <h1>Welcome To Tetris</h1>
                <?php if($notRegistered){ ?>
                    <p> error username already exists or is invalid </p>
                <?php } elseif($notLogged&&$logAttempt){ ?>
                    <P> username or password incorrect </p>
                <?php } ?>
                    <form action="index.php" method="post" id="login">
                        username: <input type="text" placeholder="Username" name="username" required><br>
                        password: <input type="password" placeholder="Password" name="password" required><br>
                        <button type="submit">Login</button><br>

                        <p>Don't have a user account?<a href="register.php">Register now</a></p><br>
                    </form>
                </div>
            <?php } ?>
        </div>
    </body>
</html>