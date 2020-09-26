class Game():

    def __init__(self):
        pass


    def rock_paper_scissors_logic(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return "It's a boring draw, try again."

        if (player_1.choice == "Rock" and player_2.choice == "Scissors") or (player_1.choice == "Paper" and player_2.choice == "Rock") or (player_1.choice == "Scissors" and player_2.choice == "Paper"):
            return player_1.name + " WINS"

        if (player_2.choice == "Rock" and player_1.choice == "Scissors") or (player_2.choice == "Paper" and player_1.choice == "Rock") or (player_2.choice == "Scissors" and player_1.choice == "Paper"):
            return player_2.name + " WINS"