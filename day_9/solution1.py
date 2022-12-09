file = open('input.txt', 'r')

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

def isDiagonal() -> bool:
    x, y = H
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if (x + dx, y + dy) == T:
            return True
    return False

for line in file:
    D, Q = line.strip().split(' ')

    dx, dy = directions[D]
    prev = H if isDiagonal() else None

    for _ in range(int(Q)):
        H = (H[0] + dx, H[1] + dy)
        
        if not isAdjacent():
            if prev != None:
                T = prev
            else:
                T = (T[0] + dx, T[1] + dy)

            trail.add(T)

        prev = H if isDiagonal() else None

print(f'Position Tail Visited {len(trail)}')


