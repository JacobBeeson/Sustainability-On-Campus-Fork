<html>
    <head>
        <link rel="stylesheet" href="SuStylesheet.css">
        <script>
            function validateform(){
                let userN = document.forms["regForm"]["username"].value;
                let passW = document.forms["regForm"]["password"].value;
                let CpassW = document.forms["regForm"]["cpassword"].value;
                
                if(passw == CpassW){
                    return true;
                } else {
                    alert("passwords must match");
                    return false;
                }

                
            }
        </script>
    </head>
    <body>
        <div class="main">
            <div>
                
                <form name="regForm" action="welcomePage.php" method="post" onsubmit="return validateform()">
                    <h1>register for PlaceHolder Name</h1>
                    Username: <input type="text" name="username" required><br>
                    Password: <input type="password" placeholder="password" name="password" required><br>
                    Confirm Password: <input type="password" placeholder="confirm password" name="cpassword" required><br>
                  Pet Name: <input type="text" name="petName" required> <br>
                    <button type="submit">Register</button>
                </form>
            </div>
        </div>
    </body>
</html>
