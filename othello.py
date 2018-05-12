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


class OthelloGame:
    def __init__(self, n=8):
        self.board = init_board(n)
        self.score = {'Player1': 2, 'Player2': 2}
        print(np.unique(self.board, return_counts=True))
        # filter the print // is it even possible :/
    def update_score(self):
        np.unique(self.board)





def main():

    game = OthelloGame()
    return




if __name__ == '__main__':
    main()
