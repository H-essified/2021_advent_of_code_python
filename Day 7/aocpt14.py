# import statistics

# Statistical approach
submarines = ([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")])
# optimal_position = int(statistics.mean(submarines)) # Statistical approach with in built libraries
optimal_position = int(sum(submarines)/len(submarines)) # Statistical approach without importing 
min_deviation = int(sum((((max(optimal_position, j) - min(optimal_position, j)) * (max(optimal_position, j) - min(optimal_position, j) + 1)))/2 for j in submarines))
print(f"Optimal position: {optimal_position}\r\nMinimum fuel spend: {min_deviation}")

# # Iterative approach
# submarines = ([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")])
# min_deviation = 0
# for i in range(min(submarines), max(submarines)):
#     deviation = int(sum((((max(i, j) - min(i, j)) * (max(i, j) - min(i, j) + 1)))/2 for j in submarines))
#     if deviation > min_deviation and i != 0:  # end iterating if deviation begins to rise
#         break
#     min_deviation, optimal_position = deviation, i
# print(f"Optimal position: {optimal_position}\r\nMinimum fuel spend: {min_deviation}")

# # Gross one-liner approach
# print(int(sum((((max(int(sum(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))/len(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))), j) - min(int(sum(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))/len(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))), j)) * (max(int(sum(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))/len(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))), j) - min(int(sum(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))/len(([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))), j) + 1)))/2 for j in ([int(item) for item in open("Day 7/input_data.txt", "r").read().split(",")]))))