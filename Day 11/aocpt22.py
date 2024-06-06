lines = [[str(value) for value in str(line).replace("\n", "")] for line in open("Day 11/input_data.txt", "r")]
octopi = {}
for x in range(10):
    for y in range(10):
        octopi[(x, y)] = int(lines[y][x])
sync_flashes = 0
i = 0
while sync_flashes != 100:
    i += 1
    sync_flashes = 0
    for point in octopi.keys():
        octopi.update({point: octopi.get(point) + 1})
    flashing = True
    flashed = []
    while flashing is True:
        flashing = False
        for point in octopi.keys():
            if point in flashed:
                continue
            if octopi.get(point) > 9:
                flashing = True
                sync_flashes += 1
                flashed.append(point)
                x = point[0]
                y = point[1]
                if y > 0:
                    if x > 0:
                        octopi.update({(x - 1, y - 1): octopi.get((x - 1, y - 1)) + 1})
                    if x < 9:
                        octopi.update({(x + 1, y - 1): octopi.get((x + 1, y - 1)) + 1})
                    octopi.update({(x, y - 1): octopi.get((x, y - 1)) + 1})
                if y < 9:
                    if x > 0:
                        octopi.update({(x - 1, y + 1): octopi.get((x - 1, y + 1)) + 1})
                    if x < 9:
                        octopi.update({(x + 1, y + 1): octopi.get((x + 1, y + 1)) + 1})
                    octopi.update({(x, y + 1): octopi.get((x, y + 1)) + 1})
                if x > 0:
                    octopi.update({(x - 1, y): octopi.get((x - 1, y)) + 1})
                if x < 9:
                    octopi.update({(x + 1, y): octopi.get((x + 1, y)) + 1})
    for point in flashed:
        octopi.update({point: 0})
print(i)