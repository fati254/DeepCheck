<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DeepCheck | Security Scan</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Fira+Code&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/scan.css">
</head>
<body>
    <nav class="topbar">
        <div class="logo"> DeepCheck</div>
        <div class="nav-links">
            <a href="scan.php" class="active">Security Scan</a>
            <a href="dashboard.php">Dashboard</a>
            <a href="#">History</a>
        </div>
        <div class="user-info">ID: <?php echo $_SESSION['username'] ?? 'GUEST'; ?></div>
    </nav>

    <div class="main">
        <div class="workspace" id="workspace">
            <div class="editor-core">
                <div class="editor-header">
                    <span>main_analysis.py</span>
                    <div class="editor-options">
                        <button class="opt-btn" onclick="document.getElementById('fileInput').click()">Upload</button>
                        <button class="opt-btn" onclick="clearEditor()">Clear</button>
                    </div>
                </div>
                <div class="editor-body">
                    <div class="line-numbers" id="lineNos">1</div>
                    <textarea id="codeEditor" spellcheck="false" oninput="updateEditor()" placeholder="Paste your code here..."></textarea>
                </div>
            </div>
            <div class="results-panel" id="resultsPanel">
                <h3>AI Analysis</h3>
                <div id="aiResponse">
                    <p>Ready for scanning. Click the button below.</p>
                </div>
            </div>
        </div>
        <div class="actions">
            <input type="file" id="fileInput" style="display:none;">
            <button class="btn-scan" onclick="startScan()">Run Deep Scan</button>
        </div>
    </div>

    <script>
        const editor = document.getElementById('codeEditor');
        const lineNos = document.getElementById('lineNos');
        const workspace = document.getElementById('workspace');

        function updateEditor() {
            const lines = editor.value.split('\n').length;
            lineNos.innerHTML = Array.from({length: lines}, (_, i) => i + 1).join('<br>');
        }
        function clearEditor() { editor.value = ''; updateEditor(); workspace.classList.remove('active'); }
        function startScan() {
            if(editor.value.trim() === "") return alert("Empty code!");
            workspace.classList.add('active');
            document.getElementById('aiResponse').innerHTML = "<p style='color:#ffbd2e;'>Analyzing vulnerabilities...</p>";
        }
    </script>
</body>
</html>