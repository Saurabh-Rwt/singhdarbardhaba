<form action="auth/login-get.php" method="POST">
    <div class="login-form">
        <h4 class="login-title">Login</h4>
        <div class="row">
            <div class="col-lg-12">
                <label>Email Address*</label>
                <input type="email" name="email" placeholder="Email Address" required>
            </div>
            <div class="col-lg-12">
                <label>Password</label>
                <input type="password" name="password" placeholder="Password" required>
            </div>
            <div class="col-sm-8 align-self-center">
                <div class="check-box">
                    <input type="checkbox" id="remember_me">
                    <label for="remember_me">Remember me</label>
                </div>  
            </div>
            <div class="col-sm-4 pt-1 mt-md-0">
                <div class="forgotton-password_info">
                    <a href="#"> Forgotten pasward?</a>
                </div>
            </div>
            <div class="col-lg-12 pt-5">
                <button class="btn custom-btn md-size" type="submit" name="login">Login</button>
            </div>
        </div>
    </div>
</form>
