from collections import Counter

file = open('./input.txt', 'r')

def findStartIndex(buffer: str, size: int) -> int:
    def isDuplicates():
        for v in found.values():
            if v > 1:
                return True
        return False

    n, res = len(buffer), -1
    found = Counter(list(buffer[:size]))
    
    for i in range(size, n):
        if not isDuplicates():
            res = i
            break
        
        j = i - size
        found[buffer[i]] += 1
        found[buffer[j]] -=1
        if found[buffer[j]] == 0:
            del found[buffer[j]]   

    return res

for line in file:
    input = line.strip()
    res = findStartIndex(input, 4)
    print(res)