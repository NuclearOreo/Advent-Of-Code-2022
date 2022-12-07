file = open('./input.txt', 'r')

partialOverlap = 0

def doesFullyOverlap(a: list[int], b: list[int]) -> bool:
    if  b[0] <= a[0] <= b[1] or b[0] <= a[1] <= b[1]:
        return True

    if a[0] <= b[0] <= a[1] or a[0] <= b[1] <= a[1]:
        return True

    return False

for line in file:
    r1, r2 = line.strip().split(',')
    r1, r2 = list(map(int, r1.split('-'))), list(map(int, r2.split('-')))

    partialOverlap += doesFullyOverlap(r1, r2)

print(f'Total Partial Overlap: {partialOverlap}')
