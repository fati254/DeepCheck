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
                    <textarea id="codeEditor" spellcheck="false" oninput="window.updateEditor()" placeholder="Paste your code here..."></textarea>
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
        console.log("JS LOADED");
    document.addEventListener("DOMContentLoaded", () => {

    
    const editor = document.getElementById('codeEditor');
    const lineNos = document.getElementById('lineNos');

   window.updateEditor = function() {
    const lines = editor.value.split("\n").length;

    let numbers = "";
    for (let i = 1; i <= lines; i++) {
        numbers += i + "<br>";
    }

    lineNos.innerHTML = numbers;
};

window.clearEditor = function() {
    
    editor.value = '';
    updateEditor();
}

    window.startScan = async function() {

        document.getElementById("workspace").classList.add("active");
        
        const resultDiv = document.getElementById("aiResponse");
       

        if (!resultDiv) {
            alert("aiResponse not found ❌");
            return;
        }

        const code = editor.value;

        if (code.trim() === "") {
            return alert("Empty code!");
        }

        resultDiv.innerHTML = "<p style='color:#ffbd2e;'>Analyzing...</p>";

        try {
            const response = await fetch("http://127.0.0.1:8000/api/scan/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ code: code })
            });

            const data = await response.json();

            console.log("DATA:", data);

            if (data && data.status === "success") {

                if (data.issues.length === 0) {
                    resultDiv.innerHTML = "<p style='color:green;'>✅ No issues found</p>";
                } else {

                    // affichage 
                    let html = "<h4 class='scan-title'>Security Issues</h4><div class='issues-list'>";
                    data.issues.forEach(issue => {
                        html += `
                         <div class="issue-card">
                           <span class="issue-icon">⚠️</span>
                           <span class="issue-text">${issue}</span>
                         </div>
                        `;
                    });
                    html += "</div>";

                    resultDiv.innerHTML = html;  
                    
                }

            } else {
                resultDiv.innerHTML = "<p style='color:red;'>Error scanning</p>";
            }

        } catch (error) {
            console.error(error);
            resultDiv.innerHTML = "<p style='color:red;'>Server error</p>";
        }
    };    

    editor.addEventListener("scroll", () => {
    lineNos.scrollTop = editor.scrollTop;
});
updateEditor();

});
</script>

</body>
</html>