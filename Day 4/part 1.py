lines = [str(line).replace("  ", " ").replace("\n", "") for line in open("input_data.txt", "r")]
call_order, cards = lines[0].split(","), {}

for i in range(1, int((len(lines)-1)/6)):
    combinations = [lines[(i * 6) + j - 4].strip().split(" ") for j in range(0, 5)]
    combinations.extend([[combination[x] for combination in combinations] for x in range(0, 5)])
    cards.update({i - 1: combinations})

for i in range(5, len(call_order)):
    called = call_order[:i]
    for key in cards.keys():
        for combination in cards.get(key):
            if sum(j in called for j in combination) == 5:
                print(sum(sum(int(number) if number not in called else 0 for number in item) for item in cards.get(key)[:5]) * int(call_order[i - 1]))
                exit()