import numpy as np

# define functions for data handling


def read_data(filename):
    with open(filename, 'r') as f:
        data = [el.strip() for el in f.readlines()]
    return data


def read_called(filename):
    data = read_data(filename)
    # extract the called numbers
    called = [int(el) for el in data[0].split(sep=",")]
    return called


def read_boards(filename):
    data = read_data(filename)
    boards = data[2:]
    return boards


def edit_boards(filename):
    boarddata = read_boards(filename)
    boards_nested = []
    board_intermediate = []
    for el in range(0, len(boarddata)):
        if len(boarddata[el]) != 0 and el != len(boarddata):
            board_intermediate.append(boarddata[el])
        elif el == len(boarddata):
            board_intermediate.append(boarddata[el])
            boards_nested.append(board_intermediate)
        else:
            boards_nested.append(board_intermediate)
            board_intermediate = []

    for ind in range(0, len(boards_nested)):
        boards_nested[ind] = [el.split() for el in boards_nested[ind]]
    return boards_nested


def board_as_class(filename):
    boarddata = edit_boards(filename)
    all_boards = [board(np.array(el).astype(int)) for el in boarddata]
    return all_boards
