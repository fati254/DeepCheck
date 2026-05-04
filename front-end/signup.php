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
    const signupForm = document.getElementById('signupForm');
    
    signupForm.addEventListener('submit', function(e) {
        const pass = document.getElementById('password').value;
        const confirmPass = document.getElementById('confirm_password').value;

        if (pass !== confirmPass) {
            e.preventDefault(); // Empêche l'envoi du formulaire
            alert("Passwords do not match! Please try again.");
        } else {
            // Ici, tu pourras ajouter ton code de connexion à la base de données plus tard
            alert("Registration successful! (Simulated)");
        }
    });
</script>