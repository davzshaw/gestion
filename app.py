from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Eso no me dio en Nodejs, asi que lo hice en flask"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
