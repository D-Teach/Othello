import numpy as np


def init_board(n=8):
    if n >= 4 and n % 2 is 0:
        board = np.zeros(shape=(n, n), dtype=np.int)
        board[int(n / 2)][int(n / 2)] = 1
        board[int(n / 2 - 1)][int(n / 2 - 1)] = 1
        board[int(n / 2 - 1)][int(n / 2)] = -1
        board[int(n / 2)][int(n / 2 - 1)] = -1
        return board
    else:
        return ValueError("Invalid board size!")


def dummy_board():

        # First number: x, second number: y
        board = np.zeros(shape=(8, 8), dtype=np.int)
        board[2][6] = 1
        board[3][6] = -1
        board[3][5] = -1
        board[3][4] = -1
        board[3][3] = -1
        board[4][3] = 1
        board[4][4] = 1
        board[4][5] = -1
        board[5][4] = 1
        board[5][5] = -1
        return board


# 1 = player1 : -1 = player2
class OthelloGame:
    def __init__(self, n=8):
        self.n = n
        self.board = init_board(n)
        self.score = {'Player1': 2, 'Player2': 2}

        return

    def update_score(self):
        self.score['Player1'] = np.count_nonzero(self.board == 1)
        self.score['Player2'] = np.count_nonzero(self.board == -1)
        return

    def is_valid(self, x, y, p):
        # North
        if x > 0 and self.board[x-1][y] == -1 * p:
            return
        # North-East
        if x > 0 and y < self.n-1 and self.board[x-1][y+1] == -1 * p:
            return
        # East
        if y < self.n-1 and self.board[x][y+1] == -1 * p:
            return
        # South-East
        if x < self.n-1 and y < self.n-1 and self.board[x+1][y+1] == -1 * p:
            return
        # South
        if x < self.n+1
        return True


    def test_valid(self):
        self.board = dummy_board()
        assert (not self.is_valid(0, 0, 1))
        assert (not self.is_valid(7, 7, -1))
        assert (self.is_valid(5, 6, 1))
        assert (self.is_valid(5, 3, -1))

        return




def main():

    #print(dummy_board())

    game = OthelloGame()
    game.test_valid()
    return


if __name__ == '__main__':
    main()
