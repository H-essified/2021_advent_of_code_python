from os import stat


lines = [str(line).replace("\n", "").strip().replace("#", "") for line in open ("Day 23/input_data.txt", "r")]
blanks = {2, 4, 6, 8}
target = {"A": {11, 12, 13, 14}, "B": {15, 16, 17, 18}, "C": {19, 20, 21, 22}, "D": {23, 24, 25, 26}}
target_top = {"A": 11, "B": 15, "C": 19, "D": 23}
costs = {"A": 1, "B": 10, "C": 100, "D": 1000}
start = lines[1]
missing_lines = ["DCBA", "DBAC"]
for i in range(4):
    for line in [lines[2]] + missing_lines + [lines[3]]:
        start += line[i]

def swap_positions(state, a, b):
    state_list = list(state)
    state_list[a], state_list[b] = state_list[b], state_list[a]
    return "".join(state_list)

def move(state):
    for position in target_top.values():
        if state[position] != "." and all(state[position + n] in (".", state[position]) for n in (1, 2, 3)) and position in target[state[position]]:
            if state[position + 1] == ".":
                if state[position + 2] == ".":
                    if state[position + 3] == ".":
                        yield swap_positions(state, position, position + 3), costs[state[position]] * 3
                    else:
                        yield swap_positions(state, position, position + 2), costs[state[position]] * 2
                else:
                    yield swap_positions(state, position, position + 1), costs[state[position]] 
    
    for target_position, position in target_top.items():
        if state[position] == "." and any(state[position + n] not in (".", target_position) for n in (1, 2, 3)):
            if state[position + 1] != ".": 
                yield swap_positions(state, position, position + 1), costs[state[position + 1]]
            elif state[position + 2] != ".":
                yield swap_positions(state, position, position + 2), costs[state[position + 2]] * 2
            else:
                yield swap_positions(state, position, position + 3), costs[state[position + 3]] * 3
    
    for position in target_top.values():
        if state[position] == ".":
            continue
        if position in target[state[position]] and all(state[position + n] in (".", state[position]) for n in (1, 2, 3)):
            continue
        h0 = (position - 11) // 2 + 2
        for hallway in range(h0 - 1, -1, -1):
            if hallway in blanks:
                continue
            if state[hallway] != ".":
                break
            yield swap_positions(state, position, hallway), costs[state[position]] * (h0 - hallway + 1)
        for hallway in range(h0 + 1, 11):
            if hallway in blanks:
                continue
            if state[hallway] != ".":
                break
            yield swap_positions(state, position, hallway), costs[state[position]] * (hallway - h0 + 1)
    
    for hallway in range(11):
        if state[hallway] == ".":
            continue
        target_position = target_top[state[hallway]]
        if state[target_position] != "." or any(state[target_position + n] not in (".", state[hallway]) for n in (1, 2, 3)):
            continue
        h0 = (target_position - 11) // 2 + 2
        if h0 > hallway and all(state[h] == "." for h in range(hallway + 1, h0)):
            yield swap_positions(state, hallway, target_position), costs[state[hallway]] * (h0 - hallway + 1)
        elif h0 < hallway and all(state[h] == "." for h in range(h0, hallway)):
            yield swap_positions(state, hallway, target_position), costs[state[hallway]] * (hallway - h0 + 1)

all_states = {start: (0, None)}
queue = {start}
while len(queue) > 0:
    state = queue.pop()
    cost = all_states[state][0]
    for next_move, next_cost in move(state):
        if next_move in all_states and all_states[next_move][0] <= cost + next_cost:
            continue
        else:
            all_states[next_move] = (cost + next_cost, state)
            queue.add(next_move)
print(all_states["...........AAAABBBBCCCCDDDD"][0])

