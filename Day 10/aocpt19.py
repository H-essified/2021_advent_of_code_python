lines = [[str(value) for value in str(line).replace("\n", "")] for line in open("Day 10/input_data.txt", "r")]
brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {"(": 3, ")": 3, "[": 57, "]": 57, "{": 1197, "}": 1197, "<": 25137, ">": 25137}
total_score = 0
for line in lines:
    close_order = ""
    for string in line:
        if string in brackets.keys():
            close_order += brackets[string]
        elif string == close_order[-1]:
            close_order = close_order[:-1]
        else:
            total_score += scores[string]
            break
print(total_score)