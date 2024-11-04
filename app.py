from flask import Flask

app = Flask(__name__)

@app.route("/")
def newflask():
    return "<h1>Welcome</h2>"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 6000)
