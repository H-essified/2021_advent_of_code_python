lines = [line.replace("\n","") for line in open("input_data.txt", "r")]
horizontal_counter, vertical_counter = 0, 0
for line in lines:
    direction = line.split(" ")[0].lower()
    distance = int(line.split(" ")[1])
    if direction == "up":
        vertical_counter -= distance
    elif direction == "down":
        vertical_counter += distance
    elif direction == "forward":
        horizontal_counter += distance
print(horizontal_counter * vertical_counter)