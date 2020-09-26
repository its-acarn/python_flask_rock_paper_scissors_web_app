import unittest
from src.player import Player
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_rock = Player("Sebastian", "Rock")
        self.player_paper = Player("Theobold", "Paper")
        self.player_scissors = Player("Barnaby", "Scissors")

        self.new_game = Game()


    def test_rock_paper_scissors_logic___player_1_wins_with__rock_v_scissors(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_rock, self.player_scissors)
        self.assertEqual("Sebastian WINS", result)


    def test_rock_paper_scissors_logic___player_1_wins_with__paper_v_rock(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_paper, self.player_rock)
        self.assertEqual("Theobold WINS", result)


    def test_rock_paper_scissors_logic___player_1_wins_with__scissors_v_paper(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_scissors, self.player_paper)
        self.assertEqual("Barnaby WINS", result)


    def test_rock_paper_scissors_logic___player_2_wins_with__scissors_v_rock(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_scissors, self.player_rock)
        self.assertEqual("Sebastian WINS", result)


    def test_rock_paper_scissors_logic___player_2_wins_with__rock_v_paper(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_rock, self.player_paper)
        self.assertEqual("Theobold WINS", result)

    
    def test_rock_paper_scissors_logic___player_2_wins_with__paper_v_scissors(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_paper, self.player_scissors)
        self.assertEqual("Barnaby WINS", result)


    def test_rock_paper_scissors_logic___draw_result_with__rock_v_rock(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_rock, self.player_rock)
        self.assertEqual("It's a boring draw, try again.", result)


    def test_rock_paper_scissors_logic___draw_result_with__paper_v_paper(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_paper, self.player_paper)
        self.assertEqual("It's a boring draw, try again.", result)

    
    def test_rock_paper_scissors_logic___draw_result_with__scissors_v_scissors(self):
        result = self.new_game.rock_paper_scissors_logic(self.player_scissors, self.player_scissors)
        self.assertEqual("It's a boring draw, try again.", result)