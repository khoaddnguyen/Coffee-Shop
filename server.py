from flask import Flask, render_template
import datetime
import requests
import os

app = Flask(__name__)
mapbox_access_token = os.environ.get("MAPBOX_ACCESS_TOKEN")

@app.route("/")
def home():
    current_year = datetime.datetime.now().year
    return render_template("index.html", year=current_year)

@app.route("/account")
def get_login():
    return render_template("login.html")

@app.route("/shop")
def get_shop():
    return render_template("shop.html")

@app.route("/play")
def get_play():
    return render_template("play.html")

@app.route("/fm")
def get_fm():
    return render_template("fm.html")

@app.route("/fm/mix")
def get_mixtapes():
    return render_template("FM-mixtapes.html")

@app.route("/test")
def get_test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True)