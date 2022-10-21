# Day 4

from calendar import c
from shutil import which


input_test = 'Data/04_test.txt'

fn = input_test

with open(fn, 'r') as f:
    data = [el.strip() for el in f.readlines()]

data

# extract the called numbers
called = [int(el) for el in data[0].split(sep=",")]
called

# extract the different boards
boards = data[2:]

boards[5]

not boards[5]

''.join(boards).split()


# extract board data and store in nested list

boards_nested = []
board_intermediate = []
for el in range(0, len(boards)):
    if len(boards[el]) != 0 and el != len(boards):
        board_intermediate.append(boards[el])
    elif el == len(boards):
        board_intermediate.append(boards[el])
        boards_nested.append(board_intermediate)
    else:
        boards_nested.append(board_intermediate)
        board_intermediate = []

for ind in range(0, len(boards_nested)):
    boards_nested[ind] = [el.split() for el in boards_nested[ind]]


#board1 = [el.split() for el in board1]

# erstelle aus den baord reihen die board spalten als liste
def vert_lists(mylist):
    out = []
    for i in range(0, len(mylist[0])):
        out.append([el[i] for el in mylist])
    return out

# erstelle die board-diagonalen


def diag_lists(mylist):
    diag1 = [mylist[ind][ind] for ind in range(0, len(mylist[0]))]
    diag2 = [mylist[::-1][ind][ind] for ind in range(0, len(mylist[0]))]
    return [diag1, diag2]


boards_vert = []

vert_lists(boards_nested[0])

boards_vert = [vert_lists(el) for el in boards_nested]
boards_diag = [diag_lists(el) for el in boards_nested]

#board1_vert = vert_lists(board1)
#board1_diag = diag_lists(board1)

board1.extend(board1_vert)
board1.extend(board1_diag)

# combine to one list with all winning options
for i in range(0, len(boards_nested)):
    boards_nested[i].extend(boards_vert[i])
    boards_nested[i].extend(boards_diag[i])
    print(f"number of win-combis: {len(boards_nested[i])}")
    print(" ------ ")

boards_int = [[[int(el) for el in sublist] for sublist in allboards]
              for allboards in boards_nested]

# Start the game
sub = boards_int[0][0]

call = called[0]

# remove element with value 17 from list sub
sub.pop(sub.index(17))

# initiate list, where matches per row are counted, all starting with zero
wins = [[[0 for el in sublist] for sublist in allboards]
        for allboards in boards_nested]

# for each match in a list, add 1 to wins
# ++ funktioniert noch nicht, weil ich nicht win und boards_nested kombinieren muss
# ++ move on here

[[[el + 1 for el in sublist if call in sublist]
    for sublist in allboards] for allboards in boards_nested]


#
