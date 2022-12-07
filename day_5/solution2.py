from collections import deque

file = open('./input.txt', 'r')

#         [J]         [B]     [T]    
#         [M] [L]     [Q] [L] [R]    
#         [G] [Q]     [W] [S] [B] [L]
# [D]     [D] [T]     [M] [G] [V] [P]
# [T]     [N] [N] [N] [D] [J] [G] [N]
# [W] [H] [H] [S] [C] [N] [R] [W] [D]
# [N] [P] [P] [W] [H] [H] [B] [N] [G]
# [L] [C] [W] [C] [P] [T] [M] [Z] [W]
#  1   2   3   4   5   6   7   8   9 

stacks = [
    deque(list('LNWTD')),
    deque(list('CPH')),
    deque(list('WPHNDGMJ')),
    deque(list('CWSNTQL')),
    deque(list('PHCN')),
    deque(list('THNDMWQB')),
    deque(list('MBRJGSL')),
    deque(list('ZNWGVBRT')),
    deque(list('WGDNPL')),  
]

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# stacks = [
#     deque(list('ZN')),
#     deque(list('MCD')),
#     deque(list('P'))
# ]

def move(q: int, c: int, n: int) -> None:
    crates = [ stacks[c-1].pop() for _ in range(q) ]
    stacks[n-1].extend(crates[::-1])

for line in file:
    tokens = line.strip().split(' ')
    q, c, n = map(int,[tokens[1], tokens[3], tokens[5]])

    move(q, c, n)

res = ''.join([s[-1] for s in stacks])
print(f'Top of Stack: {res}')