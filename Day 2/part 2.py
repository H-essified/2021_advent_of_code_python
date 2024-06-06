lines = [line.replace("\n","") for line in open("input_data.txt", "r")]
horizontal_counter, vertical_counter, aim = 0, 0, 0
for line in lines:
    direction = line.split(" ")[0].lower()
    value = int(line.split(" ")[1])
    if direction == "up":
        aim -= value
    elif direction == "down":
        aim += value
    elif direction == "forward":
        horizontal_counter += value
        vertical_counter += value * aim
print(horizontal_counter * vertical_counter)