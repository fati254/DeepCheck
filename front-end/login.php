<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Login - DeepCheck</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/auth.css?v=1.1">
</head>
<body>
<div class="background-grid"></div>
<div class="login-container">
    <a href="index.php" class="back-link">← Back to Home</a>
    <h2>Login</h2>
    <form id="loginForm">
        <div class="input-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" placeholder="Enter your email" required>
        </div>
        <div class="input-group">
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="Enter your password" required>
            <small id="togglePassword">Show Password</small>
        </div>
        <button type="submit" class="btn-login">Login</button>
        <p class="signup-text">Don't have an account? <a href="signup.php">Sign Up</a></p>
    </form>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {

    console.log("JS OK"); // test

    const passwordInput = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');
    const form = document.getElementById('loginForm');

    togglePassword.addEventListener('click', () => {
        if(passwordInput.type === 'password') {
            passwordInput.type = 'text';
            togglePassword.textContent = 'Hide Password';
        } else {
            passwordInput.type = 'password';
            togglePassword.textContent = 'Show Password';
        }
    });

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        alert("submit works"); // test important

        const email = document.getElementById('email').value.trim();
        const password = passwordInput.value.trim();

        try {
            const response = await fetch("http://127.0.0.1:8000/api/login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ 
                    email:email,
                    password: password })
            });

            const data = await response.json();

            if (data.status === "success") {
                alert("Login réussi !");
                window.location.href = "dashboard.php";
            } else {
                alert("Erreur login");
            }

        } catch (error) {
            console.error(error);
            alert("Erreur serveur");
        }
    });

});
</script>
</body>
</html>