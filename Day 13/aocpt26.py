lines = [str(line).replace("\n", "") for line in open("Day 13/input_data.txt", "r")]
points, folds = [], []
for line in lines:
    if line == "":
        continue
    elif "fold" in line:
        folds.append((line.split(" ")[2].split("=")[0], int(line.split(" ")[2].split("=")[1])))
    else:
        points.append((int(line.split(",")[0]), int(line.split(",")[1])))
for fold_order in folds:
    post_fold = []
    fold = (fold_order[0], fold_order[1])
    for point in points:
        x = point[0]
        y = point[1]
        if fold[0] == "x" and x > fold[1]:
            x = (2 * fold[1]) - x
        elif fold[0] == "y" and y > fold[1]:
            y = (2 * fold[1]) - y
        if (x, y) not in post_fold:
            post_fold.append((x, y))
    points = post_fold
for j in range(max(point[1] for point in points) + 1):
    i_points = []
    for point in points:
        if point[1] == j:
            i_points.append(point)
    i_string = ""
    for i in range(max(point[0] for point in points) + 1):
        if i in [point[0] for point in i_points]:
            i_string += "X"
        else:
            i_string += " "
    print(i_string)
