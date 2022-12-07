"""
Advent of Code 2022
--- Day 5: Supply Stacks ---
"""


with open("05_input.txt", "r") as f:
    data = f.read()

stack, commands = data.split("\n\n")
stacks = {}

for line in stack.split("\n")[-2::-1]:
    for i, e in enumerate(line[1:-1:4]):
        if e == " ":
            continue
        if i + 1 not in stacks:
            stacks[i + 1] = []
        stacks[i + 1].append(e)


stacks = stacks.copy()

# take all integer from commands and put them into a 2D list every 3 elements
nums = [int(i) for i in commands.split() if i.isdigit()]
# for loop nums by every 3 elements
nums = [nums[i:i + 3] for i in range(0, len(nums), 3)]


def solve_part1(stacks, nums):
    res = []
    for i in range(len(nums)):
        while nums[i][0] > 0 :
            temp = stacks[nums[i][1]].pop()
            stacks[nums[i][2]].append(temp)
            nums[i][0] -= 1

    for s in stacks.values():
        res.append(s[-1])
    return res


print(solve_part1(stacks, nums))