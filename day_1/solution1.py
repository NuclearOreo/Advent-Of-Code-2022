input = open('./input.txt', 'r')

total = res = 0

for line in input:
    token = line.strip()

    if token == '':
        if total > res:
            res = total
        total = 0
    else:
        total += int(token)

print(f'Largest Calories: {res}')
