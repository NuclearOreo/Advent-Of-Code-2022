from heapq import heappush, heappop

input = open('./input.txt', 'r')

topThree, total = [], 0

for line in input:
    token = line.strip()

    if token == '':
        heappush(topThree, total)
        if len(topThree) > 3: heappop(topThree)
        total = 0
    else:
        total += int(token)

print(f'Sum of top 3: {sum(map(abs, topThree))}')
