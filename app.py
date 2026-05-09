from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>RACHIDETOU ABDOU | Docker App</title>
    <style>
        body {
            background: #0a0a0f;
            color: #e2e8f0;
            font-family: monospace;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .card {
            background: #13131a;
            border: 1px solid #00e5ff;
            border-radius: 16px;
            padding: 3rem;
            text-align: center;
            max-width: 500px;
        }
        h1 { color: #00e5ff; font-size: 2rem; margin-bottom: 1rem; }
        p  { color: #94a3b8; line-height: 1.8; }
        .badge {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.4rem 1rem;
            border: 1px solid #7c3aed;
            color: #7c3aed;
            border-radius: 999px;
            font-size: 0.8rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🐳 Docker App</h1>
        <p>Bonjour à tous ! Ceci est une simple application conteneurisée avec Docker par <strong>RACHIDETOU ABDOU</strong> !</p>
        <div class="badge">Flask · Python 3.9 · Port 5000</div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)