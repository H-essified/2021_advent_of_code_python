fish_list = [int(item) for item in [str(line).replace("\n", "") for line in open("input_data.txt", "r")][0].split(",")]

fish_dict = {i: sum(j == i for j in fish_list) for i in range(9)}
for i in range(256):
    fish_dict = {j: (fish_dict.get(j + 1) if j != 8 else 0) + (fish_dict.get(0) if j == 6 or j == 8 else 0) for j in range(9)}
print(sum(fish_dict.values()))