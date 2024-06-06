hexadecimal = [str(line) for line in open("Day 16/input_data.txt", "r")][0]
binary = "".join([bin(int(bit, 16))[2:].zfill(4) for bit in hexadecimal])

def check_type(position, version_sum):
    version = int(binary[position: position + 3], 2)
    version_sum += version
    type = int(binary[position + 3: position + 6], 2)
    position += 6
    if type == 4:
        position, version_sum = find_literal(position, version_sum)
    if type != 4:
        position, version_sum = find_operator(position, version_sum)
    return position, version_sum


def find_literal(position, version_sum):
    literal_string = ""
    for j in range((len(binary) - 6) // 5):
        literal_bit = binary[position: position + 5]
        literal_string += literal_bit[1:]
        position += 5
        if literal_bit[0] == "0":
            return position, version_sum


def find_operator(position, version_sum):
    length_id = binary[position]
    position += 1
    if length_id == "0":
        sub_length = int(binary[position: position + 15], 2)
        position += 15
        start_position = position
        while position != start_position + sub_length:
            position, version_sum = check_type(position, version_sum)
        return position, version_sum
    elif length_id == "1":
        sub_length = int(binary[position: position + 11], 2)
        position += 11
        for i in range(sub_length):
            position, version_sum = check_type(position, version_sum)
        return position, version_sum

position, version_sum = check_type(0, 0)
print(version_sum)
