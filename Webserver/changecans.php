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
var_dump($_POST);


// Prepare our SQL, preparing the SQL statement will prevent SQL injection.
// $stmt = $con->prepare('SELECT title, qoh FROM cans');
// $stmt->execute();
// $var = $stmt->get_result();
// $rows = $var->fetch_all(MYSQLI_ASSOC);
// foreach ($rows as $row) {
//     printf("%s (%s)<br>", $row["title"], $row["qoh"]);

// $stmt->close();
// }
// ?>