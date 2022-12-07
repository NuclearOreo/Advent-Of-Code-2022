file = open('./input.txt', 'r')

alphabet, group = 'abcdefghijklmnopqrstuvwxyz', []
total, priorities = 0, { l: i + 1 for i, l in enumerate(alphabet + alphabet.upper()) }

def getPriority(g: list[str]) -> int:
    a, b, c = map(set, g)
    return priorities[list(a.intersection(b).intersection(c))[0]]

for line in file:
    rucksack = line.strip()
    group.append(rucksack)

    if len(group) == 3:
        total += getPriority(group)
        group = []

print(f'Total: {total}')
