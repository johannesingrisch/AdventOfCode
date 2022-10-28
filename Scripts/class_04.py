import numpy as np


class board:
    # the class defines a bingo board and methods for playing the game and
    # evaluating whether the game is won
    def __init__(self, arr):
        self.vals = arr
        self.match = np.linspace(0, 0, 25).reshape(5, 5)
        self.winstate = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.win = False
        self.sum = np.sum(self.vals)

    def call_match(self, call):
        # determine if called number is on board
        if call in self.vals:
            ind = np.where(self.vals == call)
            self.match[ind] = 1
        self.winstate[0] = list(sum(self.match))
        self.winstate[1] = list(sum(np.transpose(self.match)))

    def win_value(self):
        # is there a winner row or col?
        if 5 in self.winstate[0] or 5 in self.winstate[1]:
            self.win = True
        else:
            self.win = False

    def undrawn_sum(self):
        self.sum = np.sum(np.where(self.match == 0, self.vals, 0))

    def __str__(self):
        return f"The winstate is the following: {self.winstate}"
