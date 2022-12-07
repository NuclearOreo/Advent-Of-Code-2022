file = open('./input.txt', 'r')

mapping = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': -1, 'Y': 0, 'Z': 1 }
loses = { 'Scissors': 'Rock', 'Rock': 'Paper', 'Paper': 'Scissors' } 
beats = { 'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper' }
weights = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }
win, draw = 6, 3
score = 0

for line in file:
    opponent, state = line.strip().split(' ')
    opponent, state = mapping[opponent], mapping[state]

    if state == 1:
        score += weights[loses[opponent]] + win
    elif state == 0:
        score += weights[opponent] + draw
    else:
        score += weights[beats[opponent]] 


print(f'Total Score: {score}')    