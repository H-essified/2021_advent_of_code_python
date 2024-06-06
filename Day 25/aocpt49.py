lines = [str(line).replace("\n", "").strip() for line in open("Day 25/input_data.txt", "r")]
max_east, max_south = len(lines[0]), len(lines)
points = {(x, y): lines[y][x] for y in range(max_south) for x in range(max_east)}
moving, i = True, 0
while moving is True:
    moving = False
    for (x, y) in [(x, y) for (x, y) in points if points[(x, y)] == ">" and points[((x + 1) % max_east, y)] == "."]:
        points[(((x + 1) % max_east, y))] = points[(x, y)]
        points[(x, y)] = "."
        moving = True
    for (x, y) in [(x, y) for (x, y) in points if points[(x, y)] == "v" and points[(x, (y + 1) % max_south)] == "."]:
        points[(x, ((y + 1) % max_south))] = points[(x, y)]
        points[(x, y)] = "."
        moving = True
    i += 1
print(i)