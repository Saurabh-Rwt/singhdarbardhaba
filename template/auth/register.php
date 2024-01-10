<form action="auth/" method="POST">
    <div class="login-form">
        <h4 class="login-title">Register</h4>
        <div class="row">
            <div class="col-md-6 col-12">
                <label>First Name</label>
                <input type="text" name="first_name" placeholder="First Name" required>
            </div>
            <div class="col-md-6 col-12">
                <label>Last Name</label>
                <input type="text"  name="last_name" placeholder="Last Name" required>
            </div>
            <div class="col-md-12">
                <label>Email Address*</label>
                <input type="email"  name="email" placeholder="Email Address" required>
            </div>
            <div class="col-md-12">
                <label>Mobile Number*</label>
            </div>
            <div class="col-md-6">
                <select name="phonecode" required>
                    <option value="">Country Code</option>
                    <?php
                        include('../connection.php');
                        $query = "select * from countries";
                        $rows = mysqli_query($conn, $query);
                        foreach ($rows as $row) { ?>
                    <option value="<?php echo $row['phonecode'] ?>">
                        <?php echo  $row['name'] . "(" . $row['phonecode'] . ")" ?></option>
                    <?php } ?>
                </select>
            </div>
            <div class="col-md-6">
                <input type="number" name="phone" placeholder="Enter Mobile" required>
            </div>
            <div class="col-md-6">
                <label>State</label>
                <input type="text" name="state" placeholder="Enter State" required>
            </div>
            <div class="col-md-6">
                <label>City</label>
                <input type="text" name="city" placeholder="Enter City" required>
            </div>
            <div class="col-md-12">
                <label>Address</label>
                <input type="text" name="address" placeholder="Enter Address" required>
            </div>
            <div class="col-md-6">
                <label>Password</label>
                <input type="password" name="password" placeholder="Password" required>
            </div>
            <div class="col-md-6">
                <label>Confirm Password</label>
                <input type="password" name="confirm_password" placeholder="Confirm Password" required>
            </div>
            <div class="col-12">
                <button class="btn custom-btn md-size" name="submit">Register</button>
            </div>
        </div>
    </div>
</form>

<?php
    // include('register-get.php');
?>