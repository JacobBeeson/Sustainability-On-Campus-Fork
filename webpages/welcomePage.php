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

$dbusername = "";//connects to the database 
$dbpassword = "";
$dbname = "";

?>
<html>
    <head>
        <link rel="stylesheet" href="SusStylesheet.css">
    </head> 
    <body>
           <div class="main">
            <?php if (isset($_SESSION["userName"])) {?>
                <div>
                    <form action="tetris.php" method="get">
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