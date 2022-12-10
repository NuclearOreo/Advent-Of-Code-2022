file = open('input.txt', 'r')

snake = [(0, 0) for _ in range(10)]
trail = set([(0, 0)])
directions = { 'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0), 'TLC': (-1, -1), 'BRC': (1, 1), 'TRC': (-1, 1), 'BLC': (1, -1) }

def isAdjacent(i: int, j: int) -> bool:
    if snake[i] == snake[j]: return True
    x, y = snake[i]
    for dx, dy in directions.values():
        if (x + dx, y + dy) == snake[j]:
            return True
    return False

def getDirection(i: int, j: int) -> tuple:
    a, b = snake[i][0] - snake[j][0], snake[i][1] - snake[j][1]
    a = a if a != 0 and abs(a) == 2 else a
    if a > 1: a -= 1
    if b < -1: b += 1
    if b > 1: b -= 1
    return (a, b)

def move(D: str, Q: int) -> None:
    dx, dy = directions[D]
    
    for _ in range(Q):
        snake[0] = (snake[0][0] + dx, snake[0][1] + dy)
        
        for i in range(1, 10):
            if not isAdjacent(i - 1, i):
                a, b = getDirection(i - 1, i)
                snake[i] = (snake[i][0] + a, snake[i][1] + b)
                if i == 9: trail.add(snake[i])
            else:
                break

for line in file:
    D, Q = line.strip().split(' ')
    move(D, int(Q))

print(f'Position Tail Visited: {len(trail)}')
