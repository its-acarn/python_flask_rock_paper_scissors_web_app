import unittest
from src.player import Player
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_rock = Player("Sebastion", "Rock")
        self.player_paper = Player("Theobold", "Paper")
        self.player_scissors = Player("Barnaby", "Scissors")

        self.game_1 = Game(self.player_rock, self.player_paper)


    def test_game_has_expected_properties(self):
        self.assertEqual(self.player_rock, self.game_1.player_1)
        self.assertEqual(self.player_paper, self.game_1.player_2)


    def test_rock_paper_scissors_logic___player_1_wins_with__rock_v_scissors(self):
        result = self.game_1.rock_paper_scissors_logic(self.player_rock.choice, self.player_scissors.choice)
        self.assertEqual("Player 1 wins", result)


    def test_rock_paper_scissors_logic___player_1_wins_with__paper_v_rock(self):
        result = self.game_1.rock_paper_scissors_logic(self.player_paper.choice, self.player_rock.choice)
        self.assertEqual("Player 1 wins", result)


    def test_rock_paper_scissors_logic___player_1_wins_with__scissors_v_paper(self):
        result = self.game_1.rock_paper_scissors_logic(self.player_scissors.choice, self.player_paper.choice)
        self.assertEqual("Player 1 wins", result)

    def test_rock_paper_scissors_logic___player_2_wins_with__scissors_v_rock(self):
        result = self.game_1.rock_paper_scissors_logic(self.player_scissors.choice, self.player_rock.choice)
        self.assertEqual("Player 2 wins", result)