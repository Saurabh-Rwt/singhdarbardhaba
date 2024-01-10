<?php
session_start(); 

include('../connection.php');

if (isset($_POST['login'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    $query = "SELECT * FROM user WHERE email = '$email'";
    $result = mysqli_query($conn, $query);

    if ($result && mysqli_num_rows($result) === 1) {
        $user = mysqli_fetch_assoc($result);
        $hashed_password = $user['password'];

        if (password_verify($password, $hashed_password)) {
            $_SESSION['loggedin'] = true;
            $_SESSION['username'] = $email;

            echo "successful";
            header("Location: ../my-account.php");
            exit();
        } else {
            // Password does not match
            echo "login failed";
            // header("Location: ../cart.php");
            exit();
        }
    } else {
        // User not found
        echo "login failed";
        // header("Location: ../cart.php");
        exit();
    }
}
mysqli_close($conn);
?>
