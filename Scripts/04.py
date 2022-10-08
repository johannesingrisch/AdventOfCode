# Day 4

input_test = 'Data/04_test.txt'

fn = input_test

with open(fn, 'r') as f:
    data = [el.strip() for el in f.readlines()]

data

# extract the called numbers
called = [int(el) for el in data[0].split(sep=",")]
called

data[2:7].split(sep=",")
