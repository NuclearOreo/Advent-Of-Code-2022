file = open('./input.txt')

holdings = []
operations = []
isDivisable = []
tossTo = []

current = 0
for line in file:
    tokens = line.strip().split(' ')

    if tokens[0] == 'Monkey':
        current = int(tokens[1][:1])
        holdings.append([])
        operations.append([])
        tossTo.append([])
    elif tokens[0] == 'Starting':
        n = len(tokens)
        for i in range(2, n):
            item = int(tokens[i].strip(','))
            holdings[current].append(item)
    elif tokens[0] == 'Operation:':
        operations[current] = tokens[3:]
    elif tokens[0] == 'Test:':
        isDivisable.append(int(tokens[-1]))
    elif tokens[0] == 'If':
        tossTo[current].append(int(tokens[-1]))


rounds, numMonkeys = 20, len(holdings)
inspections = [0] * numMonkeys

def execute(val: int, ops: list[str]) -> int:
    s = ''

    for t in ops:
        if t == 'old':
            s += str(val)
        else:
            s += t

    return eval(s) // 3

for _ in range(rounds):
    
    for monkey in range(numMonkeys):

        for item in holdings[monkey]:
            inspections[monkey] += 1
            v = execute(item, operations[monkey])
            
            if v % isDivisable[monkey] == 0:
                holdings[tossTo[monkey][0]].append(v)
            else:
                holdings[tossTo[monkey][1]].append(v)
                
        holdings[monkey] = []

            


inspections.sort()
result = inspections[-1] * inspections[-2]

print(f'Monkey Business Score: {result}')

