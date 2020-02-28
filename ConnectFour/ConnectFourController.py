from ConnectFourModel import ConnectFourModel
# Connect four model to use
model = ConnectFourModel()

# Controller for connect four game


class ConnectFourController:
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
            self.input_col = input("Enter a column: ")
            if self.input_col == "q" or self.input_col == "Q":
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
        if game_over:
            self.m.print_board()
            print()
            print("Game over!", end=" ")
            if self.m.get_winner() is None:
                print("Tie Game!")
            elif self.m.get_winner().value == "R":
                print("RED wins!")
            else:
                print("YELLOW wins!")
        else:
            print("Game quit")


c = ConnectFourController(model)
c.play_game()
