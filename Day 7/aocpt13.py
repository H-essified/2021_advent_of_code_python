# import statistics

# Statistical approach
submarines = sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))
# optimal_position = int(statistics.median(submarines)) # Statistical approach with in built libraries
optimal_position = int(submarines[len(submarines) // 2]) if len(submarines) % 2 else int(sum(submarines[len(submarines) // 2 - 1: len(submarines) // 2 + 1]) / 2) # Statistical approach without importing 
min_deviation = int(sum(max(optimal_position, i) - min(optimal_position, i) for i in submarines))
print(f"Optimal position: {optimal_position}\r\nMinimum fuel spend: {min_deviation}")

# Iterative approach
# submarines = ([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")])
# min_deviation = 0
# for i in range(min(submarines), max(submarines)):
#     deviation = int(sum(max(i, j) - min(i, j) for j in submarines))
#     if deviation > min_deviation and i != 0:  # end iterating if deviation begins to rise
#         break
#     min_deviation, optimal_position = deviation, i
# print(f"Optimal position: {optimal_position}\r\nMinimum fuel spend: {min_deviation}")

# Gross one-liner approach
# print(int(sum(max(int(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))[len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2]) if len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) % 2 else int(sum(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))[len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2 - 1: len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2 + 1]) / 2), i) - min(int(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))[len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2]) if len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) % 2 else int(sum(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))[len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2 - 1: len(sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))) // 2 + 1]) / 2), i) for i in sorted(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")])))))