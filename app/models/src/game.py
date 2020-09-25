class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def rock_paper_scissors_logic(self, player_1_choice, player_2_choice):
        if player_1_choice == player_2_choice:
            return "Draw"

        if (player_1_choice == "Rock" and player_2_choice == "Scissors") or (player_1_choice == "Paper" and player_2_choice == "Rock") or (player_1_choice == "Scissors" and player_2_choice == "Paper"):
            return "Player 1 wins"

        if (player_2_choice == "Rock" and player_1_choice == "Scissors") or (player_2_choice == "Paper" and player_1_choice == "Rock") or (player_2_choice == "Scissors" and player_1_choice == "Paper"):
            return "Player 2 wins" 