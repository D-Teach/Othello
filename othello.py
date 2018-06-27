import numpy as np
import random


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
        self.turn = random.choice([1, -1])
        return

    def reset(self):
        self.board = init_board(self.n)
        self.score = {'Player1': 2, 'Player2': 2}
        self.turn = random.choice([1, -1])

    def update_score(self):
        self.score['Player1'] = np.count_nonzero(self.board == 1)
        self.score['Player2'] = np.count_nonzero(self.board == -1)
        return

    def is_valid(self, x, y, p):
        if self.board[x][y] != 0:
            return False

        # North
        if x > 1 and self.board[x-1][y] == -1 * p:
            i = 2
            while x-i > 0 and self.board[x-i][y] == -1 * p:
                i += 1
            if self.board[x-i][y] == p:
                return True

        # North-East
        if x > 1 and y < self.n-2 and self.board[x-1][y+1] == -1 * p:
            i = 2
            while x-i > 0 and y+i < self.n-1 and self.board[x-i][y+i] == -1 * p:
                i += 1
            if self.board[x-i][y+i] == p:
                return True

        # East
        if y < self.n-2 and self.board[x][y+1] == -1 * p:
            i = 2
            while y+i < self.n-1 and self.board[x][y+i] == -1 * p:
                i += 1
            if self.board[x][y+i] == p:
                return True

        # South-East
        if x < self.n-2 and y < self.n-2 and self.board[x+1][y+1] == -1 * p:
            i = 2
            while x+i < self.n-1 and y+i < self.n-1 and self.board[x+i][y+i] == -1 * p:
                i += 1
            if self.board[x+i][y+i] == p:
                return True

        # South
        if x < self.n-2 and self.board[x+1][y] == -1 * p:
            i = 2
            while x+i < self.n-1 and self.board[x+i][y] == -1 * p:
                i += 1
            if self.board[x+i][y] == p:
                return True

        # South-West
        if x < self.n-2 and y > 1 and self.board[x+1][y-1] == -1 * p:
            i = 2
            while x+i < self.n-1 and y-i > 0 and self.board[x+i][y-i] == -1 * p:
                i += 1
            if self.board[x+i][y-i] == p:
                return True

        # West
        if y > 1 and self.board[x][y-1] == -1 * p:
            i = 2
            while y-i > 0 and self.board[x][y-i] == -1 * p:
                i += 1
            if self.board[x][y-i] == p:
                return True

        # North-West
        if x > 1 and y > 1 and self.board[x-1][y-1] == -1 * p:
            i = 2
            while self.board[x-i][y-i] == -1 * p:
                i += 1
            if self.board[x-i][y-i] == p:
                return True

        return False

    def put(self, x, y, p):
        # North
        if x > 1 and self.board[x-1][y] == -1 * p:
            i = 2
            while x-i > 0 and self.board[x-i][y] == -1 * p:
                i += 1
            if self.board[x-i][y] == p:
                for k in range(0, i):
                    self.board[x-k][y] = p

        # North-East
        if x > 1 and y < self.n-2 and self.board[x-1][y+1] == -1 * p:
            i = 2
            while x-i > 0 and y+i < self.n-1 and self.board[x-i][y+i] == -1 * p:
                i += 1
            if self.board[x-i][y+i] == p:
                for k in range(0, i):
                    self.board[x-k][y+k] = p

        # East
        if y < self.n-2 and self.board[x][y+1] == -1 * p:
            i = 2
            while y+i < self.n-1 and self.board[x][y+i] == -1 * p:
                i += 1
            if self.board[x][y+i] == p:
                for k in range(0, i):
                    self.board[x][y+k] = p

        # South-East
        if x < self.n-2 and y < self.n-2 and self.board[x+1][y+1] == -1 * p:
            i = 2
            while x+i < self.n-1 and y+i < self.n-1 and self.board[x+i][y+i] == -1 * p:
                i += 1
            if self.board[x+i][y+i] == p:
                for k in range(0, i):
                    self.board[x+k][y+k] = p

        # South
        if x < self.n-2 and self.board[x+1][y] == -1 * p:
            i = 2
            while x+i < self.n-1 and self.board[x+i][y] == -1 * p:
                i += 1
            if self.board[x+i][y] == p:
                for k in range(0, i):
                    self.board[x+k][y] = p

        # South-West
        if x < self.n-2 and y > 1 and self.board[x+1][y-1] == -1 * p:
            i = 2
            while x+i < self.n-1 and y-i > 0 and self.board[x+i][y-i] == -1 * p:
                i += 1
            if self.board[x+i][y-i] == p:
                for k in range(0, i):
                    self.board[x+k][y-k] = p

        # West
        if y > 1 and self.board[x][y-1] == -1 * p:
            i = 2
            while y-i > 0 and self.board[x][y-i] == -1 * p:
                i += 1
            if self.board[x][y-i] == p:
                for k in range(0, i):
                    self.board[x][y-k] = p

        # North-West
        if x > 1 and y > 1 and self.board[x-1][y-1] == -1 * p:
            i = 2
            while self.board[x-i][y-i] == -1 * p:
                i += 1
            if self.board[x-i][y-i] == p:
                for k in range(0, i):
                    self.board[x-k][y-k] = p

    def switch_turn(self):
        for x in range(0,self.n):
            for y in range(0, self.n):
                if self.is_valid(x, y, -1 * self.turn) == True:
                    self.turn *= -1
                    return True
        for x in range(0, self.n):
            for y in range(0, self.n):
                if self.is_valid(x, y, self.turn) == True:
                    return True
        return False

    def AI_1(self):
        a = []
        b = []
        for x in range(0,self.n):
            for y in range(0, self.n):
                if self.is_valid(x, y, 1):
                    a.append((x, y))
                    b.append(self.place_check(x, y))
        m = np.argmax(b)
        p = a[m]
        self.put(p[0], p[1], 1)



    def AI_2(self):
        a = []
        for x in range(0,self.n):
            for y in range(0, self.n):
                if self.is_valid(x, y, -1):
                    a.append((x, y))
        rng = random.choice(a)
        self.put(rng[0], rng[1], -1)

    def simulate(self, show=True):
        while self.switch_turn() == True:
            if self.turn == 1:
                self.AI_1()
            else:
                self.AI_2()
            self.update_score()
            if show:
                print(self.board)
        return self.score

    def place_check(self, x, y):
        if (x is self.n-1 or x is 0) and (y is self.n-1 or y is 0):
            return 100
        elif (x > self.n-3 or x < 2) and (y > self.n-3 or y < 2):
            return 0
        elif (x is self.n-1 or x is 0) or (y is self.n-1 or y is 0):
            return 80

        return 5

    def simulate_many(self, amount):
        wolfram = 0
        andreas = 0
        for _ in range(amount):
            res = self.simulate(show=False)
            if res['Player1'] > res['Player2']:
                wolfram += 1
            else:
                andreas += 1
            self.reset()
        print("We've played ", amount," of games. Score: Wolfram ", wolfram, " - ", andreas, " Andreas")

    def test_valid(self):
        self.board = dummy_board()
        print(self.board)
        assert (not self.is_valid(0, 0, 1))
        assert (not self.is_valid(7, 7, -1))
        assert (self.is_valid(5, 6, 1))
        assert (self.is_valid(5, 3, -1))
        assert (self.is_valid(2, 4, 1))
        assert (not self.is_valid(2, 5, -1))
        assert (self.is_valid(2, 5, 1))
        return




def main():
    game = OthelloGame()
    print(game.simulate_many(1000))
    return


if __name__ == '__main__':
    main()
