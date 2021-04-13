<!Doctype html>
<html>
    <head>
        <title>Matrix Diagnostics</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-social/5.1.1/bootstrap-social.css" integrity="sha512-sopmFEmRVsWt542K+yzH3FQ1KJfdosOJG+bGLs9ZJT07b/3gUxRA9ICuJg2JtoZ9WeknAUuwJ0ggnmrV1YL6kQ==" crossorigin="anonymous" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
        <link rel="shortcut icon" href="/images/Favicon.png">
        <link rel="stylesheet" href="/static/main.css">
    </head>
    <body>
        <form method="post" action="./reportCredentials">
            <div class="row">
                <div class="col-md-6" align="center">
                    <img class="col-md-12" src="https://img1.wsimg.com/isteam/stock/4198/:/rs=w:720,h:860,cg:true,m/cr=w:720,h:860,ax:50%25,ay:50%25" alt="Matrix Diagnostics Logo">
                </div>
                <div class="col-md-6" align="center">
                    <img src="/images/matrixlogoSmall.png" alt="Matrix Diagnostics Logo" ><br>
                    <label>Patient First Name</label><br>
                    <input type="text" name="firstName" id="firstName" class="form-control" placeholder="First Name" required><br>
                    <label>Patient Last Name</label><br>
                    <input type="text" name="lastName" id="lastName" class="form-control" placeholder="Last Name" required><br>
                    <label>User Id </label><br>
                    <input type="text" name="userid" id="userid" class="form-control" placeholder="User Id" required><br>
                    <input id="login" class="button" type="submit" value="View Report">
                    <p class="gap"></p>
                    <h4>Social Links</h4>
                    <hr class="solid">
                    <a class="btn btn-social-icon btn-facebook" href="https://www.facebook.com/MatrixDiagnostics">
                        <span class="fa fa-facebook"></span>
                    </a>
                    <a class="btn btn-social-icon btn-linkedin" href="https://www.linkedin.com/MatrixDiagnostics">
                        <span class="fa fa-linkedin"></span>
                    </a>
                </div>
            </div>
        </form>
    </body>
</html>