file = open('./input.txt', 'r')

mapping = { 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors' }
beats = { 'Rock': 'Scissors', 'Paper': 'Rocks', 'Scissors': 'Paper' }
weights = { 'Rock': 1, 'Paper': 2, 'Scissors': 3 }
win, lose, draw = 6, 0, 3
score = 0

for line in file:
    player1, player2 = line.strip().split(' ')
    player1, player2 = mapping[player1], mapping[player2]

    score += weights[player2]


    if beats[player1] == player2:
        score += win
    elif beats[player2] == player1:
        score += lose
    else:
        score += draw

print(f'Total Score: {score}')
    
