# Store this code in 'app.py' file
from flask import Flask, render_template, request, redirect, url_for, session
from uplink import args
import services_api
import re
 
 
app = Flask(__name__)


@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
    args=request.args.to_dict()
    return services_api.check_login(args.get('user_name'),args.get('pass'))



@app.route('/')
@app.route('/register', methods =['GET', 'POST'])
def register():
    args=request.args.to_dict()
    return services_api.check_login(args.get('uta_id'),args.get('mail_id'),args.get('user_name'),args.get('pass'))

@app.route('/')
@app.route('/joincourse', methods =['GET', 'POST'])
def join_course_group():
    return services_api.join_course_group(args.get('uta_id'),args.get('course_id'))

@app.route('/')
@app.route('/addcoursetodb', methods =['GET', 'POST'])
def add_new_course():
    return services_api.add_course_to_db(args.get('course_id'),args.get('dept_name'))



if __name__ == "__main__":
    app.run(host ="localhost", port = int("5000"))