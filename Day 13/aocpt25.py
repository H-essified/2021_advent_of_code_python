lines = [str(line).replace("\n", "") for line in open("Day 13/input_data.txt", "r")]
points, folds = [], []
for line in lines:
    if line == "":
        continue
    elif "fold" in line:
        folds.append((line.split(" ")[2].split("=")[0], int(line.split(" ")[2].split("=")[1])))
    else:
        points.append((int(line.split(",")[0]), int(line.split(",")[1])))
post_fold = []
fold = (folds[0][0], folds[0][1])
for point in points:
    x = point[0]
    y = point[1]
    if fold[0] == "x" and x > fold[1]:
        x = (2 * fold[1]) - x
    elif fold[0] == "y" and y > fold[1]:
        y = (2 * fold[1]) - y
    if (x, y) not in post_fold:
        post_fold.append((x, y))
print(f"Number of points after first fold: {len(post_fold)}")