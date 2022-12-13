"""
Advent of Code 2022
--- Day 11: Monkey in the Middle ---
"""


from parse import compile
from tqdm import tqdm
import math

op = {"+": lambda x, y: x + y, "*": lambda x, y: x * y}

with open('11_input.txt', "r") as f:
    data = f.read()

monkeys = []


class Monkey:
    def __init__(self, number, items, operator, n, div, tm, fm):
        self.number = number
        self.items = items
        self.operator = operator
        self.n = n
        self.div = int(div)
        self.tm = int(tm)
        self.fm = int(fm)
        self.count = 0

    def operation(self, item, operator, n, worry):
        if n == 'old':
            n = item
        if operator == '+':
            return (item + int(n)) // worry
        elif operator == '-':
            return (item - int(n)) // worry
        elif operator == '*':
            return (item * int(n)) // worry
        elif operator == '/':
            return (item / int(n)) // worry

    def task(self, worry):
        if not self.has_len():
            return
        for item in reversed(self.items):
            self.count += 1
            new = self.operation(int(item), self.operator, self.n, worry)
            if new % self.div == 0:
                monkeys[self.tm].items.append(new)
                self.items.pop()
            else:
                monkeys[self.fm].items.append(new)
                self.items.pop()

    def has_len(self):
        return len(self.items) > 0


p = compile(
    """Monkey {number}:
  Starting items: {items}
  Operation: new = old {operator} {n}
  Test: divisible by {div}
    If true: throw to monkey {tm}
    If false: throw to monkey {fm}"""
)
input = [p.parse(s) for s in data.split("\n\n")]

for i in range(len(input)):
    locals()[f'monkey{i}'] = Monkey(input[i]['number'], input[i]['items'].split(','), input[i]['operator'], input[i]['n'], input[i]['div'], input[i]['tm'], input[i]['fm'])
    monkeys.append(locals()[f'monkey{i}'] )


def solve(round, monkeys, worry):
    res = []
    for i in tqdm(range(round)):
        for monkey in monkeys:
            monkey.task(worry)
    for i in range(len(monkeys)):
        res.append(monkeys[i].count)
    print(sorted(res))
    return sorted(res)[-1] * sorted(res)[-2]


print(solve(20, monkeys,3))
print(solve(10000, monkeys, 1))