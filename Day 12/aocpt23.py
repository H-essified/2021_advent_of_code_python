paths = [str(line).replace("\n", "") for line in open("Day 12/input_data.txt", "r")]
edges = [path.split("-") for path in paths]

def find_paths(path):
    starting_position = path[-1]
    if starting_position == "end":
        return 1
    i = 0
    for cave in graph[starting_position]:
        if cave == "start":
            continue
        if cave.islower() and cave in path:
            continue
        else:
            i += find_paths(path + [cave])
    return i

graph = {}
for a, b in edges:
    if a in graph.keys():
        graph[a].add(b)
    else:
        graph[a] = {b}
    if b in graph.keys():
        graph[b].add(a)
    else:
        graph[b] = {a}
path_count = find_paths(["start"])
print(path_count)
