from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD Pipeline!1"


@app.route("/test")
def new_build():
    return "New build"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
