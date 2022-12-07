from collections import defaultdict, deque

file = open('./input.txt', 'r')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
        self.dirs = {}

root = Directory('/', None)
current = root

for line in file:
    command = line.strip().split(' ')
    
    if command[0] == '$':
        if command[1] == 'cd':
            f = command[2] 
            if f == '..':
                current = current.parent
            elif f == '/':
                current = root
            else:
                if f in current.dirs:
                    current = current.dirs[f]
    else:
        if command[0] == 'dir':
            current.dirs[command[1]] = Directory(command[1], current)
        else:
            current.contents.append((int(command[0]), command[1]))
