lines = [str(line).replace("\n", "") for line in open("input_data.txt", "r")]
points = {}
for line in lines:
    x1, y1 = int(line.split(" -> ")[0].split(",")[0]), int(line.split(" -> ")[0].split(",")[1])
    x2, y2 = int(line.split(" -> ")[1].split(",")[0]), int(line.split(" -> ")[1].split(",")[1])

    if x1 == x2:  # case for vertical line
        for y in range(min([y1, y2]), max([y1, y2]) + 1):
            points.update({(x1, y): (1 if (x1, y) not in points.keys() else points.get((x1, y)) + 1)})

    elif y1 == y2:  # case for horizontal line
        for x in range(min([x1, x2]), max([x1, x2]) + 1):
            points.update({(x, y1): (1 if (x, y1) not in points.keys() else points.get((x, y1)) + 1)})

    elif max([x1, x2]) - min([x1, x2]) == max([y1, y2]) - min([y1, y2]):  # case for diagonal line
        x_min, x_max = min([x1, x2]), max([x1, x2])
        y_min, y_max = (y1 if x_min == x1 else y2), (y1 if x_max == x1 else y2)
        for i in range(x_max - x_min + 1):
            x, y = x_min + i, (y_min + i if y_min < y_max else y_min - i)
            points.update({(x, y): (1 if (x, y) not in points.keys() else points.get((x, y)) + 1)})

print(sum(i >= 2 for i in points.values()))