# Advent of Code day 3 - Part 1
input_test = 'Data/03_test.txt'
input_full = 'Data/03_full.txt'


def solve_1(fn=input_test):
    with open(fn) as f:
        diagnostics = [el[:-1] for el in f.readlines()]

    n = len(diagnostics[0])
    l = len(diagnostics)

    gamma = ""
    epsilon = ""
    for i in range(0, n):
        d = sum([int(el[i]) for el in diagnostics])
        if d/l >= 0.5:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, base=2)
    epsilon = int(epsilon, base=2)
    power = gamma * epsilon

    return power


solve_1(input_test)
