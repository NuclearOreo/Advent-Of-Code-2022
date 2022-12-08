from functools import cache

file = open('./input.txt')

grid = []

for line in file:
    token = list(map(int, list(line.strip())))
    grid.append(token)

n, m = len(grid), len(grid[0])
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
res = 0

@cache
def dive(i: int, j: int, direction: tuple) -> int:
    if 0 > i or i >= n or 0 > j or j >= m:
        return 0

    x, y = direction
    return max(grid[i][j], dive(i + x, j + y, direction))

for i in range(1, n - 1):
    for j in range(1, m - 1):
        for x, y in directions:
            if grid[i][j] > dive(i + x, j + y, (x, y)):
                res += 1
                break

res += (2 * n) + (2 * (m - 2))

print(f'Total Visible Tree: {res}')     