lines = [int(line.replace("\n","")) for line in open("input_data.txt", "r")]
print(sum(lines[i] > lines[i - 1] for i in range(1, len(lines))))