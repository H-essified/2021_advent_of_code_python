lines = [[str(value) for value in str(line).replace("\n", "")] for line in open("Day 10/input_data.txt", "r")]
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
score_values = {")": 1, "]": 2, "}": 3, ">": 4}
scores = []
for line in lines:
    close_order = []
    corrupt = False
    for string in line:
        if string in brackets.keys():
            close_order += brackets[string]
        elif string == close_order[-1]:
            close_order = close_order[:-1]
        else:
            corrupt = True
            break
    if not corrupt:
        score = 0
        for string in close_order[::-1]:
            score = (score * 5) + score_values[string]
        scores.append(score)
print(sorted(scores)[len(scores) // 2])