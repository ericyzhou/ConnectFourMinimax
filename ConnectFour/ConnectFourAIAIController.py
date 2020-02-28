from ConnectFourModel import ConnectFourModel
from Player import Player
# Connect four model to use
model = ConnectFourModel()
# Move first or second
first_or_second = 1

# Controller for playing against connect four AI


class ConnectFourAIAIController:
    input_col = None
    col = 0
    m = None

    def __init__(self, model):
        self.m = model

    def play_game(self):
        game_over = False
        while not game_over:
            self.m.print_board()
            print()
            print(self.m.get_turn().name + "'s Turn")
            self.m.ai_move()
            if self.m.is_game_over():
                game_over = True
        if game_over:
            self.m.print_board()
            print()
            print("Game over!", end=" ")
            if self.m.get_winner() == "Tie":
                print("Tie Game!")
            elif self.m.get_winner().value == "R":
                print("RED wins!")
            elif self.m.get_winner().value == "Y":
                print("YELLOW wins!")
            else:
                print("IDK")

        else:
            print("Game quit")


c = ConnectFourAIAIController(model)
c.play_game()
