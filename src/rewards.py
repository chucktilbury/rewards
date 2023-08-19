#!/usr/bin/env python3
import sqlite3
from flask import Flask, render_template, g, request
import os

app = Flask(__name__, template_folder="/home/chuck/Src/rewards/src/templates")

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template('layout.html')
    #return os.getcwd()

if __name__ == "__main__":
    app.run(debug=True)


