# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session

import re
 
 
app = Flask(__name__)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = 'Hii'
    return msg

if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))