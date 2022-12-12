file = open('./test.txt')

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


rounds, numMonkeys = 10000, len(holdings)
inspections = [0] * numMonkeys

def execute(val: int, ops: list[str]) -> int:
    a = val if ops[0] == 'old' else int(ops[0])
    b = val if ops[2] == 'old' else int(ops[2])
    
    if ops[1] == '*' or a == b:
        return val

    return a + b

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

            
print(inspections)
inspections.sort()
result = inspections[-1] * inspections[-2]

print(f'Monkey Business Score: {result}')

