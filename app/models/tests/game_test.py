import unittest
from src.player import Player
from src.game import Game
from random import randint

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_rock = Player("Sebastian", "Rock")
        self.player_paper = Player("Theobold", "Paper")
        self.player_scissors = Player("Barnaby", "Scissors")

        self.new_game = Game()


    def test_two_player_rps___player_1_wins_with__rock_v_scissors(self):
        result = self.new_game.two_player_rps(self.player_rock, self.player_scissors)
        self.assertEqual("SEBASTIAN WINS!", result)


    def test_two_player_rps___player_1_wins_with__paper_v_rock(self):
        result = self.new_game.two_player_rps(self.player_paper, self.player_rock)
        self.assertEqual("THEOBOLD WINS!", result)


    def test_two_player_rps___player_1_wins_with__scissors_v_paper(self):
        result = self.new_game.two_player_rps(self.player_scissors, self.player_paper)
        self.assertEqual("BARNABY WINS!", result)


    def test_two_player_rps___player_2_wins_with__scissors_v_rock(self):
        result = self.new_game.two_player_rps(self.player_scissors, self.player_rock)
        self.assertEqual("SEBASTIAN WINS!", result)


    def test_two_player_rps___player_2_wins_with__rock_v_paper(self):
        result = self.new_game.two_player_rps(self.player_rock, self.player_paper)
        self.assertEqual("THEOBOLD WINS!", result)

    
    def test_two_player_rps___player_2_wins_with__paper_v_scissors(self):
        result = self.new_game.two_player_rps(self.player_paper, self.player_scissors)
        self.assertEqual("BARNABY WINS!", result)


    def test_two_player_rps___draw_result_with__rock_v_rock(self):
        result = self.new_game.two_player_rps(self.player_rock, self.player_rock)
        self.assertEqual("It's a boring draw, play again.", result)


    def test_two_player_rps___draw_result_with__paper_v_paper(self):
        result = self.new_game.two_player_rps(self.player_paper, self.player_paper)
        self.assertEqual("It's a boring draw, play again.", result)

    
    def test_two_player_rps___draw_result_with__scissors_v_scissors(self):
        result = self.new_game.two_player_rps(self.player_scissors, self.player_scissors)
        self.assertEqual("It's a boring draw, play again.", result)