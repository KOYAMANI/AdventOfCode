"""
Advent of Code 2022
--- Day 4: Camp Cleanup ---
"""


def get_input(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def solve(ids):
    part1_answer = 0
    part2_answer = 0
    for line in ids:
        pair = line.split(',')
        s1 = set(range(int(pair[0].split('-')[0]), int(pair[0].split('-')[1])+1))
        s2 = set(range(int(pair[1].split('-')[0]), int(pair[1].split('-')[1])+1))
        if s1.issubset(s2) or s2.issubset(s1):  # subset
            part1_answer += 1
        if s1 & s2:  # intersection
            part2_answer += 1
    return part1_answer, part2_answer


print(solve(get_input("04_input.txt")))
