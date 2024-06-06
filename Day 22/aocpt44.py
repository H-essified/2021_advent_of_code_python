commands, cubes = [(int(command.split(" ")[1].split(",")[0][2:].split("..")[0]), int(command.split(" ")[1].split(",")[0][2:].split("..")[1]), int(command.split(" ")[1].split(",")[1][2:].split("..")[0]), int(command.split(" ")[1].split(",")[1][2:].split("..")[1]), int(command.split(" ")[1].split(",")[2][2:].split("..")[0]), int(command.split(" ")[1].split(",")[2][2:].split("..")[1]), 1 if command.split(" ")[0] == "on" else -1) for command in [str(line).replace("\n", "") for line in open("Day 22/input_data.txt", "r")]], {}

def solve(part):
    for (x0, x1, y0, y1, z0, z1, command_type) in commands:
        if part == 1 and any(item > 50 or item < -50 for item in [x0, x1, y0, y1, z0, z1]):
            continue
        update = {}
        for (cx0, cx1, cy0, cy1, cz0, cz1) in cubes.copy().keys():
            x_min, x_max, y_min, y_max, z_min, z_max = max(cx0, x0), min(cx1,x1), max(cy0, y0), min(cy1, y1), max(cz0, z0), min(cz1, z1)
            if x_min <= x_max and y_min <= y_max and z_min <= z_max:
                update[(x_min, x_max, y_min, y_max, z_min, z_max)] = -cubes[(cx0, cx1, cy0, cy1, cz0, cz1)] if (x_min, x_max, y_min, y_max, z_min, z_max) not in update.keys() else update[(x_min, x_max, y_min, y_max, z_min, z_max)] - cubes[(cx0, cx1, cy0, cy1, cz0, cz1)]
        if command_type > 0:
            update[(x0, x1, y0, y1, z0, z1)] = command_type if (x0, x1, y0, y1, z0, z1) not in update.keys() else update[(x0, x1, y0, y1, z0, z1)] + command_type
        cubes.update({item: update[item] if item not in cubes.keys() else cubes[item] + update[item] for item in update})
    return sum([cubes[cube] * ((cube[1] - cube[0] + 1) * (cube[3] - cube[2] + 1) * (cube[5] - cube[4] + 1)) for cube in cubes.keys()])

print(f"Part 1 answer: {solve(1)} \nPart 2 answer: {solve(2)}")