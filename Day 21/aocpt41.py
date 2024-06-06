lines = [str(line).replace("\n", "") for line in open("Day 21/input_data.txt", "r")]
positions = {int(line.split(" ")[1]): (int(line.split(" ")[-1]), 0) for line in lines}
rolls = 1
while positions[1][1] < 1000 and positions[2][1] < 1000:
    player = 1 if ((rolls - 1) // 3) % 2 == 0 else 2
    position = (positions[player][0] + (rolls - ((rolls % 100) * 100)) - 1) % 10 + 1
    if rolls % 3 == 0:
        positions[player] = (position, positions[player][1] + position)
    else:
        positions[player] = (position, positions[player][1])
    rolls += 1
print(min([positions[player][1] for player in [1, 2]]) * (rolls - 1))