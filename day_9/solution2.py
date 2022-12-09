file = open('test2.txt', 'r')

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

def isDiagonal(i: int, j: int) -> bool:
    x, y = snake[i]
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
        if (x + dx, y + dy) == snake[j]:
            return True
    return False

def move(D: str, Q: int) -> None:
    dx, dy = directions[D]
    
    for _ in range(Q):
        prev = snake[0] if isDiagonal(0, 1) else None
        snake[0] = (snake[0][0] + dx, snake[0][1] + dy)

        for i in range(1, 10):
            if not isAdjacent(i - 1, i):
                newPrev = snake[i] if i < 9 and isDiagonal(i, i + 1) else None
                
                if prev != None:
                    snake[i] = prev
                else:
                    snake[i] = (snake[i][0] + dx, snake[i][1] + dy)
                
                prev = newPrev
                trail.add(snake[9])
            else:
                break
        
        
        print(snake)
    
    print() 

for line in file:
    D, Q = line.strip().split(' ')

    print(D, Q)
    move(D, int(Q))
    print()

print(f'Position Tail Visited: {len(trail)}')
