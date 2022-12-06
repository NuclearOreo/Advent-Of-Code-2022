file = open('./input.txt', 'r')

mapping = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }
beats = { 'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper' }
weights = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }
win, draw = 6, 3
score = 0

for line in file:
    opponent, player = line.strip().split(' ')
    opponent, player = mapping[opponent], mapping[player]

    score += weights[player]

    if opponent == player:
        score += draw    
    elif beats[player] == opponent:
        score += win
    
print(f'Total Score: {score}')    
