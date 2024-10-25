<?php
	require_once "stripe-php-master/init.php";
	require_once "products.php";

$stripeDetails = array(
		"secretKey" => "sk_test_51P0cyISC1uYF7VhRFrgxutVOStGSXtB6yPwlTl2DrzbRQz8UXYfQW4IgTx9iDHnBzarzMqhsTIqLDHf4ExzMpMFH00toMET006",  //Your Stripe Secret key
		"publishableKey" => "pk_test_51P0cyISC1uYF7VhR3BzGwTQeUXnyl3wWjHsw69vAlh7tXoRth3feWJt7iZgugPA8VeHPN3ZP7DQu4XtRMvREU7C300x7hwUg2a"  //Your Stripe Publishable key
	);

	// Set your secret key: remember to change this to your live secret key in production
	// See your keys here: https://dashboard.stripe.com/account/apikeys
	\Stripe\Stripe::setApiKey($stripeDetails['secretKey']);

	
?>
