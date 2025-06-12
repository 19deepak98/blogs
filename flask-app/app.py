from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    API_KEY = "sk_test_51FakeKeyForGitleaksDetection"
    passwd = "password123"
    app.run(host="0.0.0.0", port=5000)
