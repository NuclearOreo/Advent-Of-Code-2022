file = open('input.txt', 'r')

res = 0
x, count = 1, 0
target = 20
cycleCount = { 'noop': 1, 'addx': 2 }

for line in file:
    tokens = line.strip().split(' ')

    for _ in range(cycleCount[tokens[0]]):
        count += 1
        if count == target:
            res += count * x
            target += 40
        
    if tokens[0] == 'addx':
        x += int(tokens[1])

print(res)
    