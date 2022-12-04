"""
Advent of Code 2022
--- Day 3: Rucksack Reorganization ---
"""

# ord('a') - ord('z') : 97 - 122 -> priority : 1-26 (-96)
# ord('A') - ord('Z') : 65 - 90 -> priority : 27-52 (-38)


def get_input(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


def solve_part1(rucksacks):
    priorities = 0
    for line in rucksacks:
        length = len(line)
        s1 = line[0:length // 2]
        s2 = line[length // 2:length]
        # Set intersection Time complexity (s1 & s2)
        # Average: O(min(len(s1), len(2)))
        # Worst: O(len(s1) * len(s2))
        group = set(s1) & set(s2)
        for c in group:
            print("The common letters are:", c)
            if c == '\n':
                continue
            elif c.islower():
                priorities += ord(c) - 96
            else:
                priorities += ord(c) - 38
    return priorities


def solve_part2(rucksacks):
    priorities = 0
    for i in range(0, len(rucksacks), 3):
        # Set intersection Time complexity (s1 & s2 ... & sn)
        # Worst: (n-1)*O(l) where l is max(len(s1),..,len(sn))
        group = set(rucksacks[i]) & set(rucksacks[i + 1]) & set(rucksacks[i + 2])
        for c in group:
            # print("The common letters are:", c)
            if c.islower():
                priorities += ord(c)-96
            else:
                priorities += ord(c)-38
    return priorities


print(solve_part1(get_input("03_input.txt")))
print(solve_part2(get_input("03_input.txt")))
