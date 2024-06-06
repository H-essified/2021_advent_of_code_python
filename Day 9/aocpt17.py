lines = [[int(value) for value in str(line).replace("\n", "")] for line in open("Day 9/input_data.txt", "r")]
risk = 0
for y in range(len(lines)):
    for x in range(len(lines[y])):
        value = lines[y][x]
        if sum([(1 if lines[y - 1][x] > value else 0) if y > 0 else 1,
        (1 if lines[y + 1][x] > value else 0) if y < len(lines) - 1 else 1,
        (1 if lines[y][x - 1] > value else 0) if x > 0 else 1,
        (1 if lines[y][x + 1] > value else 0) if x < len(lines[0]) - 1 else 1]) == 4:
            risk += 1 + value
print(f"Sum of risk values: {risk}")