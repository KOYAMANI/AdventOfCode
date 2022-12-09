"""
Advent of Code 2022
--- Day 6: Tuning Trouble ---
"""


with open("06_input.txt", "r") as f:
    data = f.read()


def solve(text, k):
    for i in range(len(text)):
        a = text[i:i+k]
        s = set(a)
        if len(s) == k:
            return i+k


print(solve(data, 4))
print(solve(data, 14))
