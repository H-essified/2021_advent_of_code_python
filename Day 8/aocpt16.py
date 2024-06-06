total_output = 0
for line in [str(line).replace("\n","") for line in open("Day 8/input_data.txt", "r")]:
    lights = {8: "abcdefg"}
    unique_values = list(dict.fromkeys("".join(sorted(value)) for value in (line.replace(" | ", " ")).split(" ")))
    for value in unique_values:
        if len(value) == 2:
            lights[1] = value
        elif len(value) == 3:
            lights[7] = value
        elif len(value) == 4:
            lights[4] = value
    for value in unique_values:
        if len(value) == 5:
            if sum(letter in value for letter in lights[1]) == 2:
                lights[3] = value
            elif sum(letter in value for letter in lights[4]) == 3:
                lights[5] = value
            else: 
                lights[2] = value
        elif len(value) == 6:
            if sum(letter in value for letter in lights[4]) == 4:
                lights[9] = value
            elif sum(letter in value for letter in lights[4]) == 3 and sum(letter in value for letter in lights[1]) == 1:
                lights[6] = value
            else: 
                lights[0] = value
    combinations = {v: k for k, v in lights.items()}
    total_output += int("".join([str(combinations[output]) for output in ["".join(sorted(item)) for item in line.split(" | ")[1].split(" ")]]))
print(f"Final output: {total_output}")