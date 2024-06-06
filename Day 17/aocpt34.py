target = [str(line).replace("\n", "").replace("target area: x=", "").replace("y=", "") for line in open("Day 17/input_data.txt", "r")][0]
x_bounds = (int(target.split(",")[0].split("..")[0]), int(target.split(",")[0].split("..")[1]))
y_bounds = (int(target.split(",")[1].split("..")[0]), int(target.split(",")[1].split("..")[1]))
optional_x_velocities, acceptable_velocities = {}, []
for initial_velocity in range(1, max(x_bounds) + 1):
    missed = False
    x_position, steps = 0, 0
    while missed == False:
        x_position = x_position + initial_velocity - steps if initial_velocity > steps else x_position
        steps += 1
        if x_position > max(x_bounds) or initial_velocity == steps and x_position < min(x_bounds):
            missed = True
        elif min(x_bounds) <= x_position <= max(x_bounds):
            if steps == initial_velocity and initial_velocity in optional_x_velocities.keys():
                over_step = [">" + str(optional_x_velocities.get(initial_velocity)[0])]
                optional_x_velocities[initial_velocity] = over_step
                missed = True
            elif initial_velocity == steps:
                optional_x_velocities[initial_velocity] = [">" + str(steps)]
                missed = True
            elif initial_velocity > steps and initial_velocity not in optional_x_velocities.keys():
                optional_x_velocities[initial_velocity] = [steps]
            else:
                over_step = optional_x_velocities[initial_velocity]
                over_step.append(steps)
                optional_x_velocities.update({initial_velocity: over_step})
for x_velocity in optional_x_velocities.keys():
    for step_count in optional_x_velocities[x_velocity]:
        missed = False
        initial_velocity = abs(min(y_bounds))
        while missed == False:
            valid = True
            y_position, steps = 0, 0
            while valid == True:
                steps += 1
                y_position += initial_velocity - steps
                if y_position < min(y_bounds):
                    initial_velocity -= 1
                    valid = False
                if initial_velocity < min(y_bounds):
                    missed = True
                if type(step_count) == str and steps >= int(step_count[1:]) and min(y_bounds) <= y_position <= max(y_bounds):
                    acceptable_velocities.append((x_velocity, initial_velocity))
                elif steps == step_count and min(y_bounds) <= y_position <= max(y_bounds):
                    acceptable_velocities.append((x_velocity, initial_velocity))
print(f"Total number of feasible shots: {len(list(dict.fromkeys(acceptable_velocities)))}")
