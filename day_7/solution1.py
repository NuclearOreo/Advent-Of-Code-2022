from collections import defaultdict, deque

file = open('./input.txt', 'r')

tree = defaultdict(dict)

for line in file:
    command = line.strip().split(' ')

    if command[0] == '$':
        if command[1] == 'cd':
            if command[2] == '..':
                current = parents[current]
            elif command[2] == '/':
                current = tree
    else:
        if command[0] == 'dir':
            parents[command[1]] = current
            current[command[1]] = defaultdict(dict)

