from flask import Flask, flash, redirect, render_template, request, url_for
from app import app
from app.models.src.player import Player
from app.models.src.game import Game

# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return render_template('welcome_page.html')

@app.route('/play', methods=['POST'])
def play():
    return render_template('play_page.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    player_1_name = request.form.get('player_1_name')
    player_1_choice = request.form.get('player_1_choice')
    player_1 = Player(player_1_name, player_1_choice)
    player_2_name = request.form.get('player_2_name')
    player_2_choice = request.form.get('player_2_choice')
    player_2 = Player(player_2_name, player_2_choice)

    new_game = Game()
    result = new_game.rock_paper_scissors_logic(player_1, player_2)
    
    return render_template('result_page.html', result=result)
