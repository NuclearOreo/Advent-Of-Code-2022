file = open('input.txt', 'r')

x, count, screen = 1, 0, ''
cycleCount = { 'noop': 1, 'addx': 2 }

for line in file:
    tokens = line.strip().split(' ')

    for _ in range(cycleCount[tokens[0]]):
        k = count % 40
        screen += '#' if k == x - 1 or k == x or k == x + 1 else '.'
        count += 1
        
    if tokens[0] == 'addx':
        x += int(tokens[1])

s, i = len(screen), 0
inc = 40

while i < s:
    print(screen[i:i + inc])
    i += inc
    