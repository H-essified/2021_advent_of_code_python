lines = [str(line).replace("\n", "") for line in open("input_data.txt", "r")]
oxygen_lines, co2_lines, j = lines, lines, 0
while len(oxygen_lines) + len(co2_lines) != 2:
    gamma_value = "1" if sum(int(oxygen_lines[i][j]) for i in range(len(oxygen_lines))) >= len(oxygen_lines)/2 else "0"
    oxygen_lines = [line for line in oxygen_lines if line[j] == gamma_value] if len(oxygen_lines) != 1 else oxygen_lines
    epsilon_value = "1" if sum(int(co2_lines[i][j]) for i in range(len(co2_lines))) < len(co2_lines)/2 else "0"
    co2_lines = [line for line in co2_lines if line[j] == epsilon_value] if len(co2_lines) != 1 else co2_lines
    j += 1
print(int(oxygen_lines[0], 2) * int(co2_lines[0], 2))
