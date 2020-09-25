import unittest
from src.player import Player
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Sebastion", "Rock")
        self.player_2 = Player("Barnaby", "Scissors")

        self.game_1 = Game(self.player_1, self.player_2)

    def test_game_has_expected_properties(self):
        self.assertEqual(self.player_1, self.game_1.player_1)
        self.assertEqual(self.player_2, self.game_1.player_2)

    def test_rock_paper_scissors_logic___player_1_wins_with__rock(self):
        result = self.game_1.rock_paper_scissors_logic(self.player_1.choice, self.player_2.choice)
        self.assertEqual("Player 1 wins",result)