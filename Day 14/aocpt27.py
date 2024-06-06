lines = [str(line).replace("\n", "") for line in open("Day 14/input_data.txt", "r")]
rules, chemicals = {}, {}
for line in lines:
    if line == "":
        continue
    elif "->" in line:
        rules.update({line.split(" -> ")[0]: line.split(" -> ")[1]})
    else:
        formula = line
for j in range(10):
    new_formula = ""
    for i in range(len(formula) - 1):
        if formula[i: i + 2] in rules.keys():
            new_formula += formula[i] + rules.get(formula[i] + formula[i + 1])
        else:
            new_formula += formula[i]
    formula = new_formula + formula[-1]
for character in "".join(set(formula)):
    chemicals[character] = formula.count(character)
print(max(chemicals.values()) - min(chemicals.values()))