lines = [[[tuple(int(v) for v in l.split(',')), set()] for l in l[1:]] for l in [l.strip().split('\n') for l in open("Day 19/input_data.txt").read().split('\n\n')]]

def find_distance(point1, point2):  # Find distance between two points
    return sum([(point1[i] - point2[i]) ** 2 for i in range(3)]) ** (1/2)


def caluculate_determinant(triple):  # Caluclate determinant to check for valid transform
    determinant = 0
    for i in range(3):
        determinant += (triple[0][i] * (triple[1][(i + 1) % 3] * triple[2][(i + 2) % 3] - triple[1][(i + 2) % 3] * triple[2][(i + 1) % 3]))
    return determinant


def orient(point, orientation):  # Reorient points
    return (point[0] * orientation[0][0] + point[1] * orientation[0][1] + point[2] * orientation[0][2], point[0] * orientation[1][0] + point[1] * orientation[1][1] + point[2] * orientation[1][2], point[0] * orientation[2][0] + point[1] * orientation[2][1] + point[2] * orientation[2][2])


def invert_matrix(matrix):  # I am sorry God
    det = caluculate_determinant(matrix)
    return ((((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1])) // det, (-((matrix[0][1] * matrix[2][2]) - (matrix[0][2] * matrix[2][1]))) // det, ((matrix[0][1] * matrix[1][2]) - (matrix[0][2] * matrix[1][1])) // det), ((-((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))) // det, ((matrix[0][0] * matrix[2][2]) - (matrix[0][2] * matrix[2][0])) // det, (-((matrix[0][0] * matrix[1][2]) - (matrix[0][2] * matrix[1][0]))) // det), (((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])) // det, (-((matrix[0][0] * matrix[2][1]) - (matrix[0][1] * matrix[2][0]))) // det, ((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])) // det))


for scanner in lines:  # Find vector distances between two scanners
    for probe1 in scanner:
        for probe2 in scanner:
            probe1[1].add(find_distance(probe1[0], probe2[0]))

beacons_map = {}  # Create dictionary of all points assessed to be identical
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        for beacon1 in lines[i]:
            for beacon2 in lines[j]:
                overlapping_points = len(beacon1[1] & beacon2[1])
                if overlapping_points >= 12:
                    if (i, j)  not in beacons_map.keys():
                        beacons_map[(i, j)] = {(beacon1[0], beacon2[0])}
                    else:
                        current_beacons = beacons_map[(i, j)]
                        current_beacons.add((beacon1[0], beacon2[0]))
                        beacons_map[(i, j)] = current_beacons

# Find all valid transformations matrices
value_options = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)] 
orientations = [(x,y,z) for x in value_options for y in value_options for z in value_options if caluculate_determinant((x,y,z)) == 1]

# Find the required transformations between beacons with known overlap
transformed = {}
for beacon, values in beacons_map.items():
    for orientation in orientations:
        transformed_set = set()
        for value in values:
            transformed_set.add(find_distance(value[0], orient(value[1], orientation)))
        if len(transformed_set) == 1:
            point1, point2 = value[0], orient(value[1], orientation)
            transformed[beacon] = [((point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]), orientation)]
            break

# Using known transformations between beacons, calculate transfomation matrices for each beacon combination
while len([*filter(lambda x: x[0] == 0, transformed)]) < len(lines) - 1:
    for b in range(len(lines)):
        for i,val1 in enumerate(lines):
            for j,val in enumerate(lines):
                if i == j or b == j:
                    continue
                if (rel1 := transformed.get((b, i))) and not transformed.get((b, j)) and (rel2 := transformed.get((i, j))):
                    transformed[(b, j)] = [*rel2, *rel1]
                if (rel1 := transformed.get((b, i))) and not transformed.get((b, j)) and (rel2 := transformed.get((j, i))):
                    transformed[(b, j)] = [*[(orient((-v[0][0], -v[0][1], -v[0][2]), inv := invert_matrix(v[1])), inv) for v in reversed(rel2)], *rel1]

# Transform each beacon to be the same orientation as beacon 0 and find Manhattan distance between points
normalised_points = []
for i in range(1, len(lines)):
    for point in lines[i]:
        zero = (0, 0, 0)
        for transform in transformed[(0,i)]:
            oriented = orient(zero, transform[1])
            zero = (transform[0][0] + oriented[0], transform[0][1] + oriented[1], transform[0][2] + oriented[2])
    normalised_points.append(zero)

print(max([sum([abs(i[0] - j[0]), abs(i[1] - j[1]), abs(i[2] - j[2])]) for i in normalised_points for j in normalised_points]))
