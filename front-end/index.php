<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>DeepCheck</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=1.1">
</head>
<body>
    <div class="background-grid"></div>
    <div class="scan-line"></div>

    <header>
    <h2 class="logo">DeepCheck</h2>
     <nav>
        <a href="#hero">Home</a>
        <a href="#how">How it works</a>
        <a href="#contact">Contact</a>
        <a href="login.php" class="btnLogin">Login</a>
     </nav>
    </header>

    <section id="hero" class="hero">
        <div class="hero-text">
            <h1>Secure Your Code</h1>
            <h2>Detect Vulnerabilities. Build Safer Systems.</h2>
            <p>Improve your code security in one click. Identify vulnerabilities, learn from mistakes, and deploy robust applications with DeepCheck.</p>
            <div class="hero-buttons">
                <a href="signup.php" class="primary"> Scan Your Project</a>
                <a href="#how" class="secondary">View Example</a>
            </div>
        </div>
    </section>

    <section id="how" class="how">
        <h2 class="section-title">How it works</h2>
        <div class="cards">
            <div class="card">
                <h3>Upload Code</h3>
                <p>Upload your project files or paste your code to start scanning.</p>
            </div>
            <div class="card">
                <h3> AI Security Analysis</h3>
                <p>Our engine scans and detects vulnerabilities instantly.</p>
            </div>
            <div class="card">
                <h3> Instant Report</h3>
                <p>Get actionable insights and secure coding recommendations.</p>
            </div>
        </div>
    </section>

    <!-- SECTION CONTACT -->
 <!-- SECTION CONTACT (English & Improved) -->
 <section id="contact" class="contact-section">
    <div class="contact-container">
        
        <div class="contact-info">
            <h2 class="section-title">Contact Team</h2>
            <p>Have questions about DeepCheck? Our team of security experts is here to assist you. We typically respond within 24 hours.</p>
            
            <div class="contact-details">
                <div class="detail-item"><strong>📍 Location:</strong> Casablanca, Morocco</div>
                <div class="detail-item"><strong>📧 Email:</strong> contact@deepcheck.ai</div>
            </div>
        </div>

        <div class="contact-card">
            <form action="process_contact.php" method="POST">
                <div class="input-group">
                    <label>Full Name</label>
                    <input type="text" name="name" placeholder="John Doe" required>
                </div>
                <div class="input-group">
                    <label>Email Address</label>
                    <input type="email" name="email" placeholder="john@example.com" required>
                </div>
                <div class="input-group">
                    <label>Message</label>
                    <textarea name="message" rows="5" placeholder="Tell us about your project..."></textarea>
                </div>
                <button type="submit" class="btn-primary">Send Message</button>
            </form>
        </div>

    </div>
 </section>
    <footer>&copy; 2026 DeepCheck Team. All rights reserved.</footer>


</body>
</html>