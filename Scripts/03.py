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


# Part 2
#  Oxygen: determine most common value in bit position, keep only elements with this value
#  if values are equal, keep 0

def oxygen_rating(diag_input):
    n = len(diag_input[0])
    l = len(diag_input)

    for ind in range(0, n):
        d = [int(el[ind]) for el in diag_input]
        if sum(d)/len(d) >= 0.5:
            diag_input = [diag_input[i]
                          for i in range(len(diag_input)) if d[i] == 1]
        else:
            diag_input = [diag_input[i]
                          for i in range(len(diag_input)) if d[i] == 0]

    rating = int(diag_input[0], base=2)
    return (rating)


def co2_rating(diag_input):
    n = len(diag_input[0])
    l = len(diag_input)

    for ind in range(0, n):
        d = [int(el[ind]) for el in diag_input]
        if sum(d)/len(d) < 0.5:
            diag_input = [diag_input[i]
                          for i in range(len(diag_input)) if d[i] == 1]
        else:
            diag_input = [diag_input[i]
                          for i in range(len(diag_input)) if d[i] == 0]
        print(diag_input)
        if len(diag_input) == 1:
            break
    rating = int(diag_input[0], base=2)
    return (rating)


def life_rating(diag_input):
    oxygen = oxygen_rating(diag_input)
    co2 = co2_rating(diag_input)
    life = oxygen * co2
    return (life)


def solve_2(fn=input_test):
    with open(fn) as f:
        diagnostics = [el[:-1] for el in f.readlines()]

    print("Life support rating:", life_rating(diagnostics))


solve_2(input_test)
solve_2(input_full)
