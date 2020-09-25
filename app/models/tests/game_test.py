import unittest
from src.player import Player
from src.game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Sebastion", "Rock")
        self.player_2 = Player("Barnaby", "Scissors")

        self.game_1 = Game(self.player_1.choice, self.player_2.choice)

    def test_game_has_expected_properties(self):
        self.assertEqual("Rock", self.game_1.player_1_choice)
        self.assertEqual("Scissors", self.game_1.player_2_choice)