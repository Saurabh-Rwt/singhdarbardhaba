

<!doctype html>
<html class="no-js" lang="zxx">

<head>
    <title>Login</title>   
    <!-- CSS -->
    <?php include('../include/css.php') ?>
</head>

<body>
<?php
    include('../connection.php');
    session_start();
    if(isset($_SESSION['loguser'])){
        header ('location: my-account.php');
    }
    else{
       header ('location: ');
    }
?>
    <!-- header -->
    <?php include('../include/header.php') ?>
    <!-- end -->

    <!--mini cart-->
    <div class="mini_cart">
        <div class="cart_gallery">
            <div class="cart_close">
                <div class="cart_text">
                    <h3>cart</h3>
                </div>
                <div class="mini_cart_close">
                    <a href="javascript:void(0)"><i class="ion-android-close"></i></a>
                </div>
            </div>
            <div class="cart_item">
                <div class="cart_img">
                    <a href="product-detail.php"><img src="assets/img/product/product1.png" alt=""></a>
                </div>
                <div class="cart_info">
                    <a href="product-detail.php">Primis In Faucibus</a>
                    <p>1 x <span> $65.00 </span></p>
                </div>
                <div class="cart_remove">
                    <a href="#"><i class="ion-android-close"></i></a>
                </div>
            </div>
            <div class="cart_item">
                <div class="cart_img">
                    <a href="product-detail.php"><img src="assets/img/product/product2.png" alt=""></a>
                </div>
                <div class="cart_info">
                    <a href="product-detail.php">Letraset Sheets</a>
                    <p>1 x <span> $60.00 </span></p>
                </div>
                <div class="cart_remove">
                    <a href="#"><i class="ion-android-close"></i></a>
                </div>
            </div>
        </div>
        <div class="mini_cart_table">
            <div class="cart_table_border">
                <div class="cart_total">
                    <span>Sub total:</span>
                    <span class="price">$125.00</span>
                </div>
                <div class="cart_total mt-10">
                    <span>total:</span>
                    <span class="price">$125.00</span>
                </div>
            </div>
        </div>
        <div class="mini_cart_footer">
            <div class="cart_button">
                <a href="cart.php">View cart</a>
            </div>
            <div class="cart_button">
                <a href="checkout.php"><i class="fa fa-sign-in"></i> Checkout</a>
            </div>
        </div>
    </div>
    <!--mini cart end-->

    <!-- page search box -->
    <div class="page_search_box">
        <div class="search_close">
            <i class="ion-close-round"></i>
        </div>
        <form class="border-bottom" action="#">
            <input class="border-0" placeholder="Search products..." type="text">
            <button type="submit"><span class="pe-7s-search"></span></button>
        </form>
    </div>

    <!-- breadcrumbs area start -->
    <div class="breadcrumbs_aree breadcrumbs_bg mb-110" data-bgimg="assets/img/others/breadcrumbs-bg.png">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="breadcrumbs_text">
                        <h1>Login | Register</h1>
                        <ul>
                            <li><a href="index.html">Home </a></li>
                            <li> // Login | Register</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- breadcrumbs area end -->
    <div class="login-register-area">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <?php include ('login.php'); ?>
                </div>
                <div class="col-lg-6 pt-5 pt-lg-0">
                    <?php include ('register.php'); ?>
                </div>
            </div>
        </div>
    </div>
    
    <!--footer-->
    <?php include('../include/footer.php') ?>
    <!--end-->

    <!-- JS -->
    <?php include('../include/javascript.php') ?>
    <!--end-->

</body>

</html>