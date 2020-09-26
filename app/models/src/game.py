class Game():

    def __init__(self):
        pass


    def two_player_rps(self, player_1, player_2):
        if player_1.choice == player_2.choice:
            return "It's a boring draw, try again."

        if (player_1.choice == "Rock" and player_2.choice == "Scissors") or (player_1.choice == "Paper" and player_2.choice == "Rock") or (player_1.choice == "Scissors" and player_2.choice == "Paper"):
            return player_1.name.upper() + " WINS!"

        if (player_2.choice == "Rock" and player_1.choice == "Scissors") or (player_2.choice == "Paper" and player_1.choice == "Rock") or (player_2.choice == "Scissors" and player_1.choice == "Paper"):
            return player_2.name.upper() + " WINS!"

    def play_computer_rps(self, player_1):
        choices = ("Rock", "Paper", "Scissors")

        computer_choice = randint(0, 2)
        
        if player_1.choice == computer_choice:
            return "It's a boring draw, try again."

        if (player_1.choice == "Rock" and computer_choice == "Scissors") or (player_1.choice == "Paper" and computer_choice == "Rock") or (player_1.choice == "Scissors" and computer_choice == "Paper"):
            return player_1.name.upper() + " WINS!"

        if (computer_choice == "Rock" and player_1.choice == "Scissors") or (computer_choice == "Paper" and player_1.choice == "Rock") or (computer_choice == "Scissors" and player_1.choice == "Paper"):
            return "COMPUTER WINS!"