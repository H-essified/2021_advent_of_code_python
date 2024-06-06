hexadecimal = [str(line) for line in open("Day 16/input_data.txt", "r")][0]
binary = "".join([bin(int(bit, 16))[2:].zfill(4) for bit in hexadecimal])

def check_type(position, value_total): 
    type = int(binary[position + 3: position + 6], 2)
    position += 6
    if type == 4:
        value, position = find_literal(position)
        return position, value
    if type != 4:
        position, values, value_total = find_operator(position, value_total)
        if type == 0:
            value_total += sum(values)
        elif type == 1:
            i = 1
            for product in values:
                i = i * product
            value_total += i
        elif type == 2:
            value_total += min(values)
        elif type == 3:
            value_total += max(values)
        elif type == 5:
            value_total += 1 if values[0] > values[1] else 0
        elif type == 6:
            value_total += 1 if values[0] < values[1] else 0
        elif type == 7:
            value_total += 1 if values[0] == values[1] else 0
        return position, value_total


def find_literal(position):
    literal_string = ""
    for j in range((len(binary) - 6) // 5):
        literal_bit = binary[position: position + 5]
        literal_string += literal_bit[1:]
        position += 5
        if literal_bit[0] == "0":
            return int(literal_string, 2), position


def find_operator(position, value_total):
    length_id = binary[position]
    position += 1
    if length_id == "0":
        sub_length = int(binary[position: position + 15], 2)
        position += 15
        start_position = position
        values = []
        while position != start_position + sub_length:
            position, value = check_type(position, value_total)
            values.append(value)
    elif length_id == "1":
        sub_length = int(binary[position: position + 11], 2)
        position += 11
        values = []
        for i in range(sub_length):
            position, value = check_type(position, value_total)
            values.append(value)
    return position, values, value_total

position, value_total = check_type(0, 0)
print(value_total)
