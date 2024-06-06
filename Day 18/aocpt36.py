lines = [str(line).replace("\n", "") for line in open("Day 18/input_data.txt", "r")]

processed = []
for processing_line in lines:
    depth, i, processed_line = 0, 0, []
    for i in range(len(processing_line)):
        if processing_line[i] == "[":
            depth += 1
        elif processing_line[i] == "]":
            depth -= 1
        elif processing_line[i] == ",":
            continue
        else:
            processed_line.append([int(processing_line[i]), depth])
    processed.append(processed_line)
  

def explode(explode_line):
    changes, pos = 0, 0
    for i in range(len(explode_line)):
        if pos == 2:
            changes += 1
            del explode_line[i - 1]
            break
        if explode_line[i][1] > 4:
            if pos == 0:
                if i != 0:
                    explode_line[i - 1] = [explode_line[i][0] + explode_line[i - 1][0], explode_line[i - 1][1]]
                explode_line[i] = [0, explode_line[i][1] - 1]
            elif pos == 1 and i != len(explode_line) - 1:
                explode_line[i + 1] = [explode_line[i][0] + explode_line[i + 1][0], explode_line[i + 1][1]]
            elif pos == 1 and i == len(explode_line) - 1:
                changes += 1
                del explode_line[i]
                break
            pos = 1 if pos == 0 else 2
    return explode_line, changes


def split(split_line):
    changes = 0
    new_line = split_line
    for i in range(len(split_line)):
        if split_line[i][0] > 9:
            changes += 1
            new_line = split_line[0: i] + [[split_line[i][0] // 2, split_line[i][1] + 1]] + [[split_line[i][0] // 2 + split_line[i][0] % 2, split_line[i][1] + 1]]
            if i < len(split_line) - 1:
                new_line.extend(split_line[i + 1:])
            break
    return new_line, changes


def find_magnitude(x, y):
    find_line = x + y
    for i in range(len(find_line)):
        find_line[i] = [find_line[i][0], find_line[i][1] + 1]
    explode_changes, split_changes = 1, 1
    while explode_changes + split_changes != 0:
        find_line, explode_changes = explode(find_line)
        if explode_changes == 0:
            find_line, split_changes = split(find_line)
    while len(find_line) != 1:
        for i in range(len(find_line)):
            if find_line[i][1] == find_line[i + 1][1]:
                find_line[i] = (find_line[i][0] * 3 + find_line[i + 1][0] * 2, find_line[i][1] - 1)
                del find_line[i + 1]
                break
    return find_line[0][0]


magnitudes = []
for x in range(len(processed)):
    for y in range(len(processed)):
        if not x == y:
            magnitudes.append(find_magnitude(processed[x], processed[y]))

print(max(magnitudes))
