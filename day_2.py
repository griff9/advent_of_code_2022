with open("inputs\input_2.txt", "r") as file:
    data = file.read()

############################# Part 1
score = 0
moves = {
    "X": {"beats": "C", "matches":'A', "scores": 1}, #rock
    "Y": {"beats": "A", "matches":'B', "scores": 2}, #paper
    "Z": {"beats": "B", "matches":'C', "scores": 3}, #scissors
}

score = 0
for round in data.split('\n'):
    foe,my_move = round.split()
    score += moves[my_move]['scores']
    if moves[my_move]['beats'] == foe:
        score += 6
    elif moves[my_move]['matches'] == foe:
        score += 3

print(f'Answer 1: {score}')

############################# Part 2
score = 0
moves = {
    "A": {"beats": "C", "loses":"B", "scores": 1}, #rock
    "B": {"beats": "A", "loses":"C", "scores": 2}, #paper
    "C": {"beats": "B", "loses":"A", "scores": 3}, #scissors
}

for round in data.split('\n'):
    foe,result = round.split()
    if result =='Y':
        score += 3 + moves[foe]['scores']
    elif result == 'Z':
        my_move = moves[foe]['loses']
        score += 6 + moves[my_move]['scores']
    else:
        my_move = moves[foe]['beats']
        score += moves[my_move]['scores']

print(f'Answer 2: {score}')
