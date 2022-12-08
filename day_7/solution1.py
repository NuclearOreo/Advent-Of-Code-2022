file = open('./input.txt', 'r')

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = {}
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
            if command[1] not in current.dirs:
                current.dirs[command[1]] = Directory(command[1], current)
        else:
            if command[1] not in current.contents:
                current.contents[command[1]] = int(command[0])

def dfs(node: Directory) -> int:    
    total = sum([ v for v in node.contents.values() ] + [ dfs(n) for n in node.dirs.values() ] + [0])

    if total <= 100000:
        res[0] += total

    return total

res = [0]
dfs(root)

print(res[0])

