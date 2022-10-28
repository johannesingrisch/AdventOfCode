# Day 4

# Part 1 -------

import numpy as np
import Scripts.funs_04 as f
from Scripts.class_04 import board


input_test = 'Data/04_test.txt'
input_full = 'Data/04_full.txt'

fn = input_full

# read called numbers
called = f.read_called(fn)

# read the bingo boards
boarddata = f.edit_boards(fn)

# transform to class 'board'
all_boards = [board(np.array(el).astype(int)) for el in boarddata]


# Playing the game ++++++

winner = 0
round = 0
while winner == 0:
    called_number = called[round]
    print(f"Round {round + 1} of the game")
    print(f"We draw number {called_number}")
    for i in range(0, len(all_boards)):
        all_boards[i].call_match(called_number)
        all_boards[i].win_value()
        if all_boards[i].win == True:
            winner += 1
            print(f"We have a winner! It is board #{i}")
            all_boards[i].undrawn_sum()
            winsum = all_boards[i].sum
            winval = winsum * called_number
            print(f"The win value is {winval}")
    round += 1
