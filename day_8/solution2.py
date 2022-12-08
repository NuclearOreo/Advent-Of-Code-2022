from functools import cache

file = open('./input.txt')

grid = []

for line in file:
    token = list(map(int, list(line.strip())))
    grid.append(token)

n, m = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
res = 0

def dive(i: int, j: int, direction: tuple, initial: int) -> int:
    if 0 > i or i >= n or 0 > j or j >= m:
        return 0

    if initial <= grid[i][j]:
        return 1

    x, y = direction
    return dive(i + x, j + y, direction, initial) + 1

maxScore = 0

for i in range(n):
    for j in range(m):
        score = 1
        for x, y in directions:
            score *= dive(i + x, j + y, (x, y), grid[i][j])

        maxScore = max(score, maxScore)

print(f'Highest Scenic Score: {maxScore}')     