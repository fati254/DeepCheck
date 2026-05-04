<head>
    <meta charset="UTF-8">
    <title>Sign Up - DeepCheck</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/auth.css?v=1.2"> 
</head>

<div class="login-container">
    <a href="index.php" class="back-link">← Back to Home</a>
    <h2>Create Account</h2>
    
    <form id="signupForm">
        <div class="input-group">
            <label>Full Name</label>
            <input type="text" id="fullname" placeholder="Enter your name" required>
        </div>

        <div class="input-group">
            <label>Email Address</label>
            <input type="email" id="email" placeholder="Enter your email" required>
        </div>

        <div class="input-group">
            <label>Password</label>
            <input type="password" id="password" placeholder="Create password" required>
        </div>

        <div class="input-group">
            <label>Confirm Password</label>
            <input type="password" id="confirm_password" placeholder="Confirm password" required>
        </div>

        <button type="submit" class="btn-login">Sign Up</button>
    </form>

    <p class="signup-text">
        Already have an account? <a href="login.php">Sign In</a>
    </p>
</div>

<script>
document.addEventListener("DOMContentLoaded", () => {

    const signupForm = document.getElementById('signupForm');

    signupForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = document.getElementById('fullname').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const confirmPass = document.getElementById('confirm_password').value;

        if (password !== confirmPass) {
            alert("Passwords do not match!");
            return;
        }

        console.log("sending signup..."); // DEBUG

        try {
            const response = await fetch("http://127.0.0.1:8000/api/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password
                })
            });

            const data = await response.json();

            console.log("response:", data); // DEBUG

            if (data.status === "ook") {
                alert("Account created successfully!");
                window.location.href = "login.php";
            } else {
                alert("Signup error");
            }

        } catch (error) {
            console.error(error);
            alert("Server error");
        }
    });

});
</script>