"""
Advent of Code 2022
--- Day 6: Tuning Trouble ---
"""


with open("06_input.txt", "r") as f:
    data = f.read()


def solve_part1(text):
    for i in range(len(text)):
        a = text[i:i+4]
        s = set(a)
        if len(s) == 4:
            return i+4


def solve_part2(text):
    for i in range(len(text)):
        a = text[i:i+14]
        s = set(a)
        if len(s) == 14:
            return i+14


print(solve_part1(data))
print(solve_part2(data))