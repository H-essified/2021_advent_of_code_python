lines = [str(line).replace("\n", "") for line in open("Day 21/input_data.txt", "r")]
starting_positions = [int(line.split(" ")[-1]) for line in lines]

def roll_die(player_1_position, player_2_position, player_1_score=0, player_2_score=0, player=0, cache={}):
    if (player_1_position, player_2_position, player_1_score, player_2_score, player) in cache:
        return cache[(player_1_position, player_2_position, player_1_score, player_2_score, player)]
    wins = [0, 0]
    rolls = [i + j + k for i in [1, 2, 3] for j in [1, 2, 3] for k in [1, 2, 3]]
    for roll in rolls:
        positions = [player_1_position, player_2_position]
        scores = [player_1_score, player_2_score]
        positions[player] = (positions[player] + roll - 1) % 10 + 1
        scores[player] += positions[player]
        if scores[player] >= 21:
            wins[player] += 1
        else:
            wins1, wins2 = roll_die(positions[0], positions[1], scores[0], scores[1], 1 if player == 0 else 0)
            wins[0] += wins1
            wins[1] += wins2
    cache[(player_1_position, player_2_position, player_1_score, player_2_score, player)] = wins
    return wins

print(max(roll_die(starting_positions[0], starting_positions[1])))    