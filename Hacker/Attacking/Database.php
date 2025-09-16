<?php
$host = "localhost";
$user = "root";
$password = "abebaws";

$conn = mysqli_connect($host, $user, $password);
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

mysqli_query($conn, "CREATE DATABASE IF NOT EXISTS TryH");
mysqli_select_db($conn, "TryH");

$sql = "
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
)
";

mysqli_query($conn, $sql);
mysqli_close($conn);
?>
