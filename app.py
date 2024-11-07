from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def newflask():
    return "<h1>Welcome</h2>"

@app.route("/test")
def newdev():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)
