target = [str(line).replace("\n", "").replace("target area: x=", "").replace("y=", "") for line in open("Day 17/input_data.txt", "r")][0]
x_bounds = (int(target.split(",")[0].split("..")[0]), int(target.split(",")[0].split("..")[1]))
y_bounds = (int(target.split(",")[1].split("..")[0]), int(target.split(",")[1].split("..")[1]))
optional_x_velocities = {}
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
step_count = min(optional_x_velocities[min(optional_x_velocities.keys())])
initial_velocity - abs(min(y_bounds))
while True:
    valid = True
    y_position, steps, max_y_position = 0, 0, 0
    while valid == True:
        steps += 1
        y_position += initial_velocity - steps
        max_y_position = y_position if y_position > max_y_position else max_y_position
        if y_position < min(y_bounds):
            initial_velocity -= 1
            valid = False
        if steps >= int(step_count[1:]) and min(y_bounds) <= y_position <= max(y_bounds):
            print(f"Max vertical distance: {max_y_position}")
            exit()