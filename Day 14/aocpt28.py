lines = [str(line).replace("\n", "") for line in open("Day 14/input_data.txt", "r")]
rules = {}
for line in lines:
    if "->" in line:
        rules.update({line.split(" -> ")[0]: line.split(" -> ")[1]})
    elif len(line) > 0:
        formula = line
pairs, chemicals = {}, {formula[0]: 1, formula[-1]: 1}
for i in range(len(formula) - 1):
    if formula[i: i + 2] in pairs.keys():
        pairs.update({formula[i: i + 2]: pairs.get(formula[i: i + 2]) + 1})
    else:
        pairs[formula[i: i + 2]] = 1
for i in range(40):
    new_pairs = {}
    for pair in pairs.keys():
        for couplet in [pair[0] + rules.get(pair), rules.get(pair) + pair[1]]:
            if couplet in new_pairs:
                new_pairs.update({couplet: new_pairs.get(couplet) + pairs.get(pair)})
            else:
                new_pairs[couplet] = pairs.get(pair)
    pairs = new_pairs
for key in pairs.keys():
    for chemical in key:
        if chemical not in chemicals:
            chemicals[chemical] = pairs.get(key)
        else:
            chemicals.update({chemical: chemicals.get(chemical) + pairs.get(key)})

print(max(chemicals.values()) // 2- min(chemicals.values()) // 2)