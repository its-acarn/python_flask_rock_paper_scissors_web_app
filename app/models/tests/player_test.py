import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player_1 = Player("Sebastian", "Rock")

    def test_player_has_properties(self):
        self.assertEqual("Sebastian", self.player_1.name)
        self.assertEqual("Rock", self.player_1.choice)