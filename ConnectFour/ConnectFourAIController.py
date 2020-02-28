from ConnectFourModel import ConnectFourModel
from Player import Player
# Connect four model to use
model = ConnectFourModel()
# Move first or second
first_or_second = 1

# Controller for playing against connect four AI


class ConnectFourAIController:
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
            if ((self.m.get_turn() is Player.RED and first_or_second == 1) or (self.m.get_turn() is Player.YELLOW and first_or_second == 2)):
                self.input_col = input("Enter a column: ")
                if self.input_col == "q" or self.input_col == "Q":
                    print(self.input_col)
                    print("Quitting")
                    break
                try:
                    self.col = int(self.input_col) - 1
                    try:
                        self.m.move(self.col)
                        if self.m.is_game_over():
                            game_over = True
                    except ValueError:
                        print("Invalid move, try again")
                except ValueError:
                    print("Invalid input, try again")
            else:
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


c = ConnectFourAIController(model)
c.play_game()
