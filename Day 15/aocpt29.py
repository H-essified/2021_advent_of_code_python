lines = [str(line).replace("\n", "") for line in open("Day 15/input_data.txt", "r")]
diameter = len(lines)
cheapest_route = {(0, 0): 0}
iterable_positions = [(0, 0)]
while len(iterable_positions) != 0:
    new_positions = []
    for position in iterable_positions:
        x, y = position[0], position[1]
        neighbours = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
        positional_cost = cheapest_route[position]
        for neighbour in neighbours:
            if neighbour[0] >= diameter * 5 or neighbour[1] >= diameter * 5 or neighbour[0] < 0 or neighbour[1] < 0:
                continue
            j = neighbour[1] - (neighbour[1] // diameter * diameter)
            i = neighbour[0] - (neighbour[0] // diameter * diameter)
            neighbour_cost = int(lines[j][i]) + neighbour[0] // diameter + neighbour[1] // diameter
            if neighbour_cost > 9:
                neighbour_cost = neighbour_cost - ((neighbour_cost // 9) * 9)
            total_cost_to_neighbour = positional_cost + neighbour_cost
            if neighbour in cheapest_route.keys() and total_cost_to_neighbour >= cheapest_route[neighbour]:
                continue
            else:
                cheapest_route[neighbour] = total_cost_to_neighbour
                new_positions.append(neighbour)
    iterable_positions = new_positions
print(cheapest_route[((diameter * 5) - 1, (diameter * 5) - 1)])