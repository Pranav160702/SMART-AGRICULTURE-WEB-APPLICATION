# Agriculture Portal

The Agriculture Portal is a machine learning-powered platform developed to support farmers with data-driven predictions and actionable insights. Key features include:

- Crop and Fertilizer Recommendations: Predicts optimal crops and suggests fertilizers tailored to specific conditions, helping farmers maximize yield.
- Disease Detection: Identifies potential crop diseases early, assisting in proactive management and treatment.
 Rainfall and Yield Forecasting: Provides rainfall and yield predictions to aid in planning and resource allocation.
- Direct Crop Sales: Facilitates direct crop sales to customers through a secure payment gateway powered by Stripe API.
- Additional Resources:
  - A chatbot powered by OpenAI’s GPT-3.5-turbo model for on-demand assistance.
  - A 4-day weather forecast powered by a Weather API to help with daily planning.
  - Real-time agriculture news provided via the News API.
- This comprehensive portal empowers farmers to make well-informed decisions, optimize crop health, and expand market access.

## Pre Requisites
### Get Below API Keys
- [News API](https://newsapi.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [Stripe API](https://dashboard.stripe.com/account/apikeys)
- [OpenAI API](https://platform.openai.com/account/api-keys)

### Gmail SMTP Setup
1. Setup  [app password for gmail](https://support.google.com/accounts/answer/185833?hl=en)
2. Open `fsend_otp.php` and `csend_otp.php` files and change username and password.

```php
function smtp_mailer($to,$subject, $msg){
	require_once("../smtp/class.phpmailer.php");
	$mail = new PHPMailer(); 
	$mail->IsSMTP(); 
	$mail->SMTPDebug = 0; 
	$mail->SMTPAuth = TRUE; 
	$mail->SMTPSecure = 'ssl'; 
	$mail->Host = "smtp.gmail.com";
	$mail->Port = 465; 
	$mail->IsHTML(true);
	$mail->CharSet = 'UTF-8';
	$mail->Username = "username@gmail.com";    // Change it to yours email address
        $mail->Password = "password"; 	
        $mail->SetFrom("username@gmail.com");   // App Password, (16 character Key)
	$mail->Subject = $subject;
	$mail->Body =$msg;
	$mail->AddAddress($to);
	if(!$mail->Send()){
		return 0;
	}else{
		return 1;
	}
}
```

## Installation

1. Clone the repository to your local machine.
```bash
git clone [https://github.com/Pranav160702/SMART-AGRICULTURE-WEB-APPLICATION.git]
```
2. Goto Farmers folder and Install the required packages using pip.
```
pip install -r requirements.txt
```
3. Change Success Url and Cancel Url file paths in `customer/cbuy_crops.php`.
```php
$session = \Stripe\Checkout\Session::create([
'payment_method_types' => ['card'],
	'line_items' => [[
	'price_data' => [
		'product' => 'prod_NdAYaoDLX3DnMY',
		'unit_amount' => $TotalCartPrice,
		'currency' => 'inr',
		],
		'quantity' => 1,
		]],
	'mode' => 'payment',
	'success_url' => 'http://localhost/projects/agri2/customer/cupdatedb.php',   // Change File Path
	'cancel_url' => 'http://localhost/projects/agri2/customer/cbuy_crops.php',   // Change File Path
]);
```
4. Add API Keys to respective files.
- News API Key to `fnewsfeed.php`
- OpenWeatherMap API Key to `fweather_forecast.php`
- Stripe API Key to `customer/stripePayment/config.php`
- OpenAI API Key to `index.php` and `fchatgpt.php`
5. Import database from db folder.
6. Run Apache web server using XAMPP.

## Features
- Crop Prediction
- Crop Recommendation
- Fertilizer Recommendation
- Rainfall Prediction
- Disease Prediction
- Yield Prediction
- OTP Verification through mail
- Agriculture realetd news using News API
- Chatbot using OpenAI's gpt-3.5-turbo model
- Dynamically changing quotes using OpenAI's API
- Weather Forecast upto 4 days using OpenWeatherMap API
- Direct crop sales to customer with real time payment interface using Stripe API


## Technologies Used
- Python
- PHP
- Pandas
- NumPy
- JavaScript
- HTML/CSS
- Bootstrap4
- Scikit-learn

## Dataset
The Crop Management System dataset includes the following features:

### Crop Prediction Dataset
- State_Name
- District_Name
- Season
- Crop

### Crop Recommendation Dataset
- N
- P
- K
- Temperature
- Humidity
- pH
- Rainfall
- Label

### Fertilizer Recommendation Dataset
- Temparature
- Humidity
- Soil Moisture
- Soil Type
- Crop Type
- Nitrogen
- Phosphorous
- Potassium
- Fertilizer Name

### Rainfall Prediction Dataset
- SUBDIVISION
- YEAR
- JAN
- FEB
- MAR
- APR
- MAY
- JUN
- JUL
- AUG
- SEP
- OCT
- NOV
- DEC
- ANNUAL
- Jan-Feb
- Mar-May
- Jun-Sep
- Oct-Dec

### Yield Prediction Dataset
- State_Name
- District_Name
- Crop_Year
- Season
- Crop
- Area
- Production

## How to Use
- Crop Prediction: Input `State_Name`, `District_Name`, and `Season` to get the predicted crop for that location.
- Crop Recommendation: Input `N`, `P`, `K`, `Temperature`, `Humidity`, `pH`, and `Rainfall` for that location to get recommended crops for that location.
- Fertilizer Recommendation: Input `Temperature`, `Humidity`, `Soil Moisture`, `Soil Type`, `Crop Type`, `Nitrogen`, `Phosphorous`, and `Potassium` to get recommended fertilizer for that crop and location.
- Rainfall Prediction: Input `Subdivision` and `Year` to get rainfall prediction for that year.
- Yield Prediction: Input `State_Name`, `District_Name`, `Crop_Year`, `Season`, `Crop`, `Area`, `Production` to get predicted yields for that crop and location.


