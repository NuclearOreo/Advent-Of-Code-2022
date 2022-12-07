file = open('./input.txt', 'r')

alphabet = 'abcdefghijklmnopqrstuvwxyz'
total, priorities = 0, { l: i + 1 for i, l in enumerate(alphabet + alphabet.upper()) }

for line in file:
    rucksack = line.strip()
    half = len(rucksack) // 2

    a, b = set(rucksack[:half]), set(rucksack[half:])

    for item in a:
        if item in b:
            total += priorities[item]

print(total)

