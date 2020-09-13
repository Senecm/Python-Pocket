from flask import Flask #, redirect, url

#creating an instance of flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hey Gamer</h1>"

if __name__ == "__main__":
    app.run()