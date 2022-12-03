"""
Advent of Code 2022
--- Day 1: Calorie Counting ---
"""

import csv

# import csv as a list
with open('01_input.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

# for loop the list and store each sum in the dictionary
backpack = []
localSum = 0

for i in range(len(data)):
    if len(data[i]) != 0:
        localSum += int(data[i][0])
        backpack.append(localSum)
    else:
        localSum = 0

backpack.sort()

# max value in the dictionary
print(backpack[-1])

# sum of top 3 values in the dictionary
print(sum(backpack[-3:]))
