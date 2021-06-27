
<?php
// We need to use sessions, so you should always start sessions using the below code.
session_start();
// If the user is not logged in redirect to the login page...
if (!isset($_SESSION['loggedin'])) {
	header('Location: index.html');
	exit;
}
// Database info
$DATABASE_HOST = 'localhost';
$DATABASE_USER = 'admin';
$DATABASE_PASS = 'admin';
$DATABASE_NAME = 'DCIS';
// Database connection
$con = mysqli_connect($DATABASE_HOST, $DATABASE_USER, $DATABASE_PASS, $DATABASE_NAME);
if ( mysqli_connect_errno() ) {
	// If there is an error with the connection, stop the script and display the error.
	exit('Failed to connect to MySQL: ' . mysqli_connect_error());
}

// Prepare our SQL, preparing the SQL statement will prevent SQL injection.
$stmt = $con->prepare('SELECT title, qoh FROM cans');
$stmt->execute();
$var = $stmt->get_result();
$rows = $var->fetch_all(MYSQLI_ASSOC);
foreach ($rows as $row) {
    printf("%s (%s)<br>", $row["title"], $row["qoh"]);
	}

$stmt->close();
?>


<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Home Page</title>
		<link href="stylesheet.css" rel="stylesheet" type="text/css">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css">
	</head>
	<body class="loggedin">
		<nav class="navtop">
			<div>
				<h1>DICSIPS Inventory System</h1>
				<a href="home.php"><i class="fas fa-home"></i>Home</a>
				<a href="inventory.php"><i class="fas fa-archive"></i>Inventory</a>
				<a href="logout.php"><i class="fas fa-sign-out-alt"></i>Logout</a>
				
			</div>
		</nav>
		<div class="content">
			<h2>Can Inventory Counts</h2>
			<div>
			<form action="changecans.php" method="post">
				<fieldset class="inlineform">
					<h1>TEST TITLE</h1>
					<label for="currentamount">Current Amount:</label><br>
					<input type="number" id="countinput" name="countbox"><br>
					<input type="submit" value="Submit">
				</fieldset>
			</form>
			<form action="changecans.php" method="post">
				<fieldset class="inlineform">
					<h1>TEST TITLE</h1>
					<label for="currentamount">Current Amount:</label><br>
					<input type="number" id="countinput" name="countbox"><br>
					<input type="submit" value="Submit">
				</fieldset>
			</form>
			</div>
		</div>
	</body>
</html>