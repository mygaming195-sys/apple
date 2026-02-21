from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Deployment Success</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>🚀 Hey! It is working bro!</h1>
            <p><strong>Server:</strong> {socket.gethostname()}</p>
            <p><strong>Time:</strong> {datetime.datetime.now()}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return "healthy", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)