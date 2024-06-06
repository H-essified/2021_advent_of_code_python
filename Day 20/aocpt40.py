lines =[str(line).replace("\n", "").replace(".", "0").replace("#", "1") for line in open("Day 20/input_data.txt", "r")]
image_raw = ["0" * (len(lines[2]) + 4)] * 2 + ["00" + line + "00" for line in lines[2:]] + ["0" * (len(lines[2]) + 4)] * 2

for iteration in range(50):
    filler = "0" if iteration % 2 == 1 else "1"
    enhanced_image = [filler * (len(image_raw[0]) + 2)] * 2
    for y in range(1, len(image_raw) - 1):
        enhanced_string = filler * 2
        for x in range(1, len(image_raw) - 1):
            enhanced_string += lines[0][int("".join([line[x - 1: x + 2] for line in image_raw[y - 1: y + 2]]), 2)]
        enhanced_image.append(enhanced_string + filler * 2)
    image_raw = enhanced_image + [filler * (len(image_raw[0]) + 2)] * 2

print(sum([sum(line[x] == "1" for x in range(len(line))) for line in image_raw]))