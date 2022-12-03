"""
Advent of Code 2022
--- Day 2: Rock Paper Scissors ---
"""

import csv
with open('02_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# --- Part One ---
total = 0

wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
loses = {'X': 'B', 'Y': 'C', 'Z': 'A'}
draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
score = {'X': 1, 'Y': 2, 'Z': 3}

for i in range(len(data)):
    data[i] = data[i][0].split(' ')
    if draw[data[i][1]] == data[i][0]:
        total += 3 + score[data[i][1]]
    elif wins[data[i][1]] == data[i][0]:
        total += 6 + score[data[i][1]]
    elif loses[data[i][1]] == data[i][0]:
        total += 0 + score[data[i][1]]

print(total)

# --- Part Two ---

total = 0
for i in range(len(data)):
    if data[i][1] == 'X':
        total += 0 + score[data[i][1]]
        if data[i][0] == 'A': # Z
            total += 3
        if data[i][0] == 'B': # X
            total += 1
        if data[i][0] == 'C':# Y
            total += 2
    elif data[i][1] == 'Y':
        total += 3
        if data[i][0] == 'A': # X
            total += 1
        if data[i][0] == 'B': # Y
            total += 2
        if data[i][0] == 'C':# Z
            total += 3
    elif data[i][1] == 'Z':
        total += 6
        if data[i][0] == 'A': # Y
            total += 2
        if data[i][0] == 'B': # Z
            total += 3
        if data[i][0] == 'C':# X
            total += 1

print(total)