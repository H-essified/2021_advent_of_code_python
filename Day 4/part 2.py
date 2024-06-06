lines = [str(line).replace("  ", " ").replace("\n", "") for line in open("input_data.txt", "r")]
call_order, cards = lines[0].split(","), {}

for i in range(1, int((len(lines)-1)/6)):  # compute all possible winning combinations for each bingo card
    combinations = [lines[(i * 6) + j - 4].strip().split(" ") for j in range(0, 5)]
    combinations.extend([[combination[x] for combination in combinations] for x in range(0, 5)])
    cards.update({i - 1: combinations})
remaining_cards, winning_cards = cards.keys(), []

for i in range(5, len(call_order)):  # iterate through called numbers to remove winners
    called = call_order[:i]
    for key in cards.keys():
        for combination in cards.get(key):
            if sum(j in called for j in combination) == 5:  # winning condition
                winning_cards.append(key)
                continue
    remaining_cards = []
    for key in cards.keys():  # create list of cards which haven't won
        if key not in winning_cards:
            remaining_cards.append(key)
    if len(remaining_cards) == 0:  # end scenario
        print(sum(sum(int(number) if number not in called else 0 for number in item) for item in cards.get(winning_card)[:5]) * int(call_order[i - 1]))
        exit()
    else:
        winning_card = remaining_cards[0]