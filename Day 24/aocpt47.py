blocks = [block.split("\n") for block in open("Day 24/input_data.txt", "r").read().split("inp w\n")[1:]]
monad_max, queue = [0] * 14, []
for i, block in enumerate(blocks):
    if block[3] == "div z 1":
        queue.append((i, int(block[14].split(" ")[-1])))
    else:
        j, x = queue.pop()
        difference = x + int(block[4].split(" ")[-1])
        if difference < 0:
            i, j, difference = j, i, -difference
        monad_max[i], monad_max[j] = 9, 9 - difference
print("".join([str(i) for i in monad_max]))