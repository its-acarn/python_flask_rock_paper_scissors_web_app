from flask import Flask, flash, redirect, render_template, request, url_for
from app import app
from random import randint
from app.models.src.player import Player
from app.models.src.game import Game
from random import randint


@app.route('/')
def index():
    return redirect(url_for('welcome'))


@app.route('/welcome', methods=['POST', 'GET'])
def welcome():
    return render_template('welcome_page.html')


@app.route('/play', methods=['POST'])
def play():
    return render_template('play_page.html')


@app.route('/play-pc', methods=['POST'])
def play_pc():
    return render_template('play_pc_page.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    player_1_name = request.form.get('player_1_name')
    player_1_choice = request.form.get('player_1_choice')
    player_1 = Player(player_1_name, player_1_choice)
    player_2_name = request.form.get('player_2_name')
    player_2_choice = request.form.get('player_2_choice')
    player_2 = Player(player_2_name, player_2_choice)

    new_game = Game()
    result = new_game.two_player_rps(player_1, player_2)
    
    return render_template('result_page.html', player_1_name=player_1_name, player_1_choice=player_1_choice, player_2_name=player_2_name, player_2_choice=player_2_choice, result=result)


@app.route('/result-pc', methods=['POST', 'GET'])
def result_pc():
    player_1_name = request.form.get('player_1_name')
    player_1_choice = request.form.get('player_1_choice')
    player_1 = Player(player_1_name, player_1_choice)
    
    choices = ("Rock", "Paper", "Scissors")
    computer_choice = choices[randint(0, 2)]
    
    player_2_name = 'COMPUTER'
    player_2_choice = computer_choice
    player_2 = Player(player_2_name, player_2_choice)

    new_game = Game()
    result = new_game.two_player_rps(player_1, player_2)
    
    return render_template('result_pc_page.html', player_1_name=player_1_name, player_1_choice=player_1_choice, computer_choice=player_2_choice, result_pc=result)

@app.route('/<player_1_choice>/<player_2_choice>', methods=['POST', 'GET'])
def url_play(player_1_choice, player_2_choice):
    player_1_name = 'Player 1'
    player_2_name = 'Player 2'
    player_1 = Player(player_1_name, player_1_choice.capitalize())
    player_2 = Player(player_2_name, player_2_choice.capitalize())
    new_game = Game()
    result = new_game.two_player_rps(player_1, player_2)
    
    return render_template('result_page.html', player_1_name=player_1_name, player_1_choice=player_1_choice, player_2_name=player_2_name, player_2_choice=player_2_choice, result=result)

