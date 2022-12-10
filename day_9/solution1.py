file = open('test1.txt', 'r')

H, T = (0, 0), (0, 0)
trail = set([(0, 0)])
directions = { 'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0), 'TLC': (-1, -1), 'BRC': (1, 1), 'TRC': (-1, 1), 'BLC': (1, -1) }

def isAdjacent() -> bool:
    if H == T: return True
    x, y = H
    for dx, dy in directions.values():
        if (x + dx, y + dy) == T:
            return True
    return False

def getDirection() -> tuple:
    a, b = H[0] - T[0], H[1] - T[1]
    if a < -1: a += 1
    if a > 1: a -= 1
    if b < -1: b += 1
    if b > 1: b -= 1
    return (a, b)

for line in file:
    D, Q = line.strip().split(' ')
    dx, dy = directions[D]

    for _ in range(int(Q)):
        H = (H[0] + dx, H[1] + dy)

        if not isAdjacent():
            a, b = getDirection()
            T = (T[0] + a, T[1] + b)

        trail.add(T)

print(f'Position Tail Visited {len(trail)}')
