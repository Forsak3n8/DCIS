<?php
// Database info
$DATABASE_HOST = 'localhost';
$DATABASE_USER = 'admin';
$DATABASE_PASS = 'admin';
$DATABASE_NAME = 'DICSIPS';
// Database connection
$con = mysqli_connect($DATABASE_HOST, $DATABASE_USER, $DATABASE_PASS, $DATABASE_NAME);
if ( mysqli_connect_errno() ) {
	// If there is an error with the connection, stop the script and display the error.
	exit('Failed to connect to MySQL: ' . mysqli_connect_error());
}

// Prepare our SQL, preparing the SQL statement will prevent SQL injection.
$stmt = $con->prepare('SELECT title, qoh FROM cans');
$stmt->execute();
$stmt->bind_result($var);
$var = $stmt->fetch();
var_dump($var);
?>