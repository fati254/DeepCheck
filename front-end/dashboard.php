<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DeepCheck | Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/dashboard.css">
</head>
<body>
    <nav class="topbar">
        <div class="logo"> DeepCheck</div>
        <div class="nav-links">
            <a href="scan.php">Security Scan</a>
            <a href="dashboard.php" class="active">Dashboard</a>
            <a href="#">History</a>
        </div>
        <div class="user-status">SEC_OPS: ACTIVE</div>
    </nav>

    <div class="container">
        <h1>Security Dashboard</h1>
        <p class="subtitle">Overview of your code security posture.</p>

        <div class="stats-grid">
            <div class="stat-card">
                <span>Total Scans</span>
                <h2>12</h2>
            </div>
            <div class="stat-card critical">
                <span>Critical Issues</span>
                <h2>02</h2>
            </div>
            <div class="stat-card">
                <span>Average Score</span>
                <h2>85%</h2>
            </div>
        </div>

        <div class="activity-section">
            <h3>Recent Activity</h3>
            <table class="history-table">
                <thead>
                    <tr>
                        <th>File Name</th>
                        <th>Date</th>
                        <th>Vulnerabilities</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>login_system.php</td>
                        <td>Mar 30, 2026</td>
                        <td class="risk-text">1 SQL Injection</td>
                        <td><span class="badge failed">FAILED</span></td>
                    </tr>
                    <tr>
                        <td>api_connect.js</td>
                        <td>Mar 28, 2026</td>
                        <td class="safe-text">Clean</td>
                        <td><span class="badge secure">SECURE</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>