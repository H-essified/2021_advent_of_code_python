lines = [[int(value) for value in str(line).replace("\n", "")] for line in open("Day 9/input_data.txt", "r")]
all_points, clusters = [], []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] != 9:
            all_points.append((x, y))
for point in all_points:
    expansion, current_cluster = [point], 1
    all_points.remove(point)
    while len(expansion) != 0:
        new_points = []
        for x, y in expansion:
            for i, j in[(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (i, j) in all_points:
                    new_points.append((i, j))
                    all_points.remove((i, j))
        current_cluster += len(new_points)
        expansion = new_points
    clusters.append(current_cluster)
basin_products = sorted(clusters)[-3] * sorted(clusters)[-2] * sorted(clusters)[-1]
print(f"Total product: {basin_products}")