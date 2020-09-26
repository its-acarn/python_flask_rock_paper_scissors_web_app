from flask import Flask, flash, redirect, render_template, request, url_for
from app import app

# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return redirect(url_for('play'))

@app.route('/welcome')
def welcome():
    return render_template('welcome_page.html')

@app.route('/play')
def play():
    return render_template('play_page.html')

@app.route('/result', methods=['POST'])
def result():

    print(request.form)
    return "Done"
    # return render_template('result_page.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'secret':
#             error = 'Invalid credentials'
#         else:
#             flash('You were successfully logged in')
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)