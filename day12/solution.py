from collections import deque

with open('12_input.txt', "r") as f:
    data = f.read().strip()
lines = [x for x in data.split('\n')]

Map = []
for line in lines:
    Map.append(line)

R = len(Map)
C = len(Map[0])

# Save the ord of each letter
OrdMap = [[0 for _ in range(C)] for _ in range(R)]
for r in range(R):
    for c in range(C):
        if Map[r][c] == 'S':
            OrdMap[r][c] = 1
        elif Map[r][c] == 'E':
            OrdMap[r][c] = 26
        else:
            OrdMap[r][c] = ord(Map[r][c])-ord('a')+1


def solve_part1():
    Q = deque()
    for r in range(R):
        for c in range(C):
            if Map[r][c]=='S':
                Q.append(((r,c), 0))

    S = set()
    while Q:
        (r, c),d = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if Map[r][c]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and OrdMap[rr][cc]<=1+OrdMap[r][c]:
                Q.append(((rr,cc),d+1))


def solve_part2():
    Q = deque()
    for r in range(R):
        for c in range(C):
            if OrdMap[r][c] == 1:
                Q.append(((r,c), 0))

    S = set()
    while Q:
        (r, c),d = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if Map[r][c]=='E':
            return d
        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            rr = r+dr
            cc = c+dc
            if 0<=rr<R and 0<=cc<C and OrdMap[rr][cc]<=1+OrdMap[r][c]:
                Q.append(((rr,cc),d+1))

print(solve_part1())
print(solve_part2())