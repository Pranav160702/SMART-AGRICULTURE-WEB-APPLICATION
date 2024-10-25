<?php
session_start();
require('../sql.php'); // Includes Login Script

if(isset($_SESSION['farmer_login_user'])) {
    $email = $_SESSION['farmer_login_user'];
    $res = mysqli_query($conn, "SELECT * FROM farmerlogin WHERE email = ?");
    mysqli_stmt_bind_param($res, "s", $email);
    mysqli_stmt_execute($res);
    $count = mysqli_stmt_num_rows($res);

    if ($count > 0) {
        $otp = rand(11111, 99999);
        $stmt = mysqli_prepare($conn, "UPDATE farmerlogin SET otp = ? WHERE email = ?");
        mysqli_stmt_bind_param($stmt, "is", $otp, $email);
        mysqli_stmt_execute($stmt);

        $html = "Your OTP verification code for Agriculture Portal is " . $otp;
        if (smtp_mailer($email, 'OTP Verification', $html)) {
            echo "yes";
        } else {
            echo "email_error";
        }
    } else {
        echo "not_exist";
    }
} else {
    echo "session_error";
}

function smtp_mailer($to, $subject, $msg) {
    require_once("../smtp/class.phpmailer.php");
    $mail = new PHPMailer();
    $mail->IsSMTP();
    $mail->SMTPDebug = 0;
    $mail->SMTPAuth = TRUE;
    $mail->SMTPSecure = 'tls';
    $mail->Host = "smtp.gmail.com";
    $mail->Port = 465;//587;
    $mail->IsHTML(true);
    $mail->CharSet = 'UTF-8';
	$mail->Username = "agricultureportal16@gmail.com";   
    $mail->Password = "zasyuatvwdphwnml"; 	
    $mail->SetFrom("agricultureportal16@gmail.com");  
    $mail->Subject = $subject;
    $mail->Body = $msg;
    $mail->AddAddress($to);
    if (!$mail->Send()) {
        return false;
    } else {
        return true;
    }
}
?>
