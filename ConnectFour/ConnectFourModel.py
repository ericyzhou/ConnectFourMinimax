from Player import Player
import time
import math

# Model for connect four game against minimax AI with alpha beta pruning
# Takes too long for any board size bigger than 4x4
x_size = 4
y_size = 4


class ConnectFourModel:
    board = []
    turn = Player.RED

    def __init__(self):
        self.board = [[None for x in range(x_size)] for y in range(y_size)]
        self.turn = Player.RED

    def move(self, col):
        if self.is_game_over():
            raise ValueError("Game is over")
        elif 0 <= col < y_size:
            if has_slot(self.board[col]):
                for ind in range(0, x_size):
                    if self.board[col][ind] is None:
                        self.board[col][ind] = self.turn.value
                        self.turn = get_other(self.turn)
                        return
            else:
                raise ValueError("Column full")
        else:
            raise ValueError("Invalid column")

    def ai_move(self):
        if self.is_game_over():
            raise ValueError("Game is over")
        else:
            start_time = time.time()
            (score, px, py) = self.max_alpha_beta(-2, 2)
            print("Algorithm took", time.time() - start_time, "seconds")
            self.board[px][py] = self.turn.value
            self.turn = get_other(self.turn)

    def max_alpha_beta(self, alpha, beta):
        best_score = -2
        px = None
        py = None

        check_win = self.get_winner()
        if check_win == "Tie":
            return (0, 0, 0)
        elif check_win is self.turn:
            return (1, 0, 0)
        elif check_win is get_other(self.turn):
            return (-1, 0, 0)

        for col in range(0, y_size):
            for ind in range(0, x_size):
                if self.board[col][ind] is None:
                    self.board[col][ind] = self.turn.value
                    score = self.min_alpha_beta(alpha, beta)[0]
                    if score > best_score:
                        best_score = score
                        px = col
                        py = ind
                    self.board[col][ind] = None
                    break
            if best_score >= beta:
                return (best_score, px, py)

            if best_score > alpha:
                alpha = best_score

        return (best_score, px, py)

    def min_alpha_beta(self, alpha, beta):
        best_score = 2
        px = None
        py = None

        check_win = self.get_winner()
        if check_win == "Tie":
            return (0, 0, 0)
        elif check_win is self.turn:
            return (1, 0, 0)
        elif check_win is get_other(self.turn):
            return (-1, 0, 0)

        for col in range(0, y_size):
            for ind in range(0, x_size):
                if self.board[col][ind] is None:
                    self.board[col][ind] = get_other(self.turn).value
                    score = self.max_alpha_beta(alpha, beta)[0]
                    if score < best_score:
                        best_score = score
                        px = col
                        py = ind
                    self.board[col][ind] = None
                    break
            if best_score <= alpha:
                return (best_score, px, py)

            if best_score < beta:
                beta = best_score

        return (best_score, px, py)

    def get_turn(self):
        return self.turn

    def is_game_over(self):
        if is_full(self.board):
            return True
        elif check_four(self.board, "R"):
            return True
        elif check_four(self.board, "Y"):
            return True
        else:
            return False

    def get_winner(self):
        if self.is_game_over():
            if check_four(self.board, Player.RED.value):
                return Player.RED
            elif check_four(self.board, Player.YELLOW.value):
                return Player.YELLOW
            else:
                return "Tie"
        else:
            return None

    def print_board(self):
        for x in range(x_size - 1, -1, -1):
            print("| ", end="")
            for y in range(0, y_size):
                if self.board[y][x] is None:
                    print("_", end=" | ")
                else:
                    print(self.board[y][x], end=" | ")
            print()
        for _ in range(0, (y_size * 4) + 1):
            print("=", end="")
        print()
        print("| ", end="")
        for z in range(1, y_size + 1):
            print(z, end=" | ")

    def get_board(self):
        return self.board


def get_other(turn):
    if turn is Player.RED:
        return Player.YELLOW
    else:
        return Player.RED


def check_four(arr, p):
    for x in range(0, len(arr)):
        for y in range(0, len(arr[0])):
            if (diagonal_check(arr, x, y, p, 0) or
                horizontal_check(arr, x, y, p, 0) or
                    vertical_check(arr, x, y, p, 0)):
                return True
    return False


def diagonal_check(arr, x, y, p, count):
    return diagonal_check_left(arr, x, y, p, 0) or diagonal_check_right(arr, x, y, p, 0)


def diagonal_check_left(arr, x, y, p, count):
    if count == 4:
        return True
    elif x < 0 or x > x_size - 1 or y < 0:
        return False
    elif (arr[x][y] == p and diagonal_check(arr, x - 1, y - 1, p, count + 1)):
        return True
    else:
        return False


def diagonal_check_right(arr, x, y, p, count):
    if count == 4:
        return True
    elif x < 0 or x > x_size - 1 or y < 0:
        return False
    elif (arr[x][y] == p and diagonal_check(arr, x + 1, y - 1, p, count + 1)):
        return True
    else:
        return False


def horizontal_check(arr, x, y, p, count):
    if count == 4:
        return True
    elif x > x_size - 1:
        return False
    elif (arr[x][y] == p and horizontal_check(arr, x + 1, y, p, count + 1)):
        return True
    else:
        return False


def vertical_check(arr, x, y, p, count):
    if count == 4:
        return True
    elif y < 0:
        return False
    elif (arr[x][y] == p and vertical_check(arr, x, y - 1, p, count + 1)):
        return True
    else:
        return False


def is_full(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] is None:
                return False
    return True


def has_slot(arr):
    for slot in arr:
        if slot is None:
            return True
    return False
