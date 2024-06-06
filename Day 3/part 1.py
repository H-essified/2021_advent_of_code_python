# # Efficient method
lines = [str(line).replace("\n", "") for line in open("input_data.txt", "r")]
gamma = "".join("1" if sum(int(lines[i][j]) for i in range(len(lines))) >= len(lines)/2 else "0" for j in range(12))
print(int(gamma, 2) * int("".join("1" if x == "0" else "0" for x in gamma), 2))

# Less efficient method
# lines = [str(line).replace("\n", "") for line in open("input_data.txt", "r")]
# print(int("".join("1" if sum(int(lines[i][j]) for i in range(len(lines))) >= len(lines)/2 else "0" for j in range(12)), 2) * int("".join("1" if sum(int(lines[i][j]) for i in range(len(lines))) <= len(lines)/2 else "0" for j in range(12)), 2) )

# Super inefficient method
# print(int("".join("1" if sum(int([str(line).replace("\n", "") for line in open("input_data.txt", "r")][i][j]) for i in range(len([str(line).replace("\n", "") for line in open("input_data.txt", "r")]))) >= len([str(line).replace("\n", "") for line in open("input_data.txt", "r")])/2 else "0" for j in range(12)), 2) * int("".join("1" if sum(int([str(line).replace("\n", "") for line in open("input_data.txt", "r")][i][j]) for i in range(len([str(line).replace("\n", "") for line in open("input_data.txt", "r")]))) <= len([str(line).replace("\n", "") for line in open("input_data.txt", "r")])/2 else "0" for j in range(12)), 2) )
