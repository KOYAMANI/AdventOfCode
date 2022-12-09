"""
Advent of Code 2022
--- Day 8: Treetop Tree House ---
"""

# This is inefficient solution but tried to solve without any libraries :)

with open('08_input.txt', "r") as f:
    data = f.read().splitlines()

matrix = []
for i in range(len(data)):
    matrix.append([])
    for l in data[i]:
        matrix[i].append(int(l))

print('the matrix has ' + str(len(matrix)) + ' rows and ' + str(len(matrix[0])) + ' columns')


def solve_part1(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i == 0 or j == 0 or i == len(matrix)-1 or j == len(matrix)-1:
                count += 1
            elif matrix[i][j] > max(matrix[i][k] for k in range(j))\
            or matrix[i][j] > max(matrix[i][k] for k in range(j+1, len(matrix)))\
            or matrix[i][j] > max(matrix[k][j] for k in range(i))\
            or matrix[i][j] > max(matrix[k][j] for k in range(i+1, len(matrix))):
                count += 1
    return count


def solve_part2(matrix):
    res = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            up, down, left, right = 0, 0, 0, 0
            for k in reversed(range(j)):
                up += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
            for k in range(j+1, len(matrix)):
                left += 1
                if matrix[i][k] >= matrix[i][j]:
                    break
            for k in reversed(range(i)):
                down += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
            for k in range(i+1, len(matrix)):
                right += 1
                if matrix[k][j] >= matrix[i][j]:
                    break
            res = max(res, up*down*left*right)
    return res


print(f"Part 1: {solve_part1(matrix)}")
print(f"Part 2 {solve_part2(matrix)}")
