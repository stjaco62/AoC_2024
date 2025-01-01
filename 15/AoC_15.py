import re

def get_data(filename):
    l_map = []
    movements = ""
    t = "map"
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if t == "map":
                if line == "":
                    t = "move"
                else:
                    row = []
                    for chr in line:
                        row.append(chr)
                    l_map.append(row)
            else:
                movements += line
    return l_map, movements

def move_robot(line):
    rgx = r"(\.)(O*@)"
    return re.sub(rgx, "\\2\\1", line)

def move_robot_left(l_map):
    for row_ind, row in enumerate(l_map):
        line = "".join(row)
        if "@" in line:
            line = move_robot(line)
            l_map[row_ind] = list(line)
            return l_map

def move_robot_right(l_map):
    for row_ind, row in enumerate(l_map):
        line = "".join(row)
        if "@" in line:
            line = line[::-1]
            line = move_robot(line)
            line = line[::-1]
            l_map[row_ind] = list(line)
            return l_map

def move_robot_up(l_map):
    for row_ind, row, in enumerate(l_map):
        line = "".join(row)
        if "@" in line:
            col_ind = line.index("@")
            line2 = ""
            for row in l_map:
                line2 += row[col_ind]
            line2 = move_robot(line2)
            for row_ind2, row2 in enumerate(l_map):
                l_map[row_ind2][col_ind] = line2[row_ind2]
            return l_map

def move_robot_down(l_map):
    for row_ind, row, in enumerate(l_map):
        line = "".join(row)
        if "@" in line:
            col_ind = line.index("@")
            line2 = ""
            for row in l_map:
                line2 += row[col_ind]
            line2 = line2[::-1]
            line2 = move_robot(line2)
            line2 = line2[::-1]
            for row_ind2, row2 in enumerate(l_map):
                l_map[row_ind2][col_ind] = line2[row_ind2]
            return l_map

def calculate_score(l_map):
    score = 0
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col == "O":
                score += 100 * row_ind + col_ind
    return score

# Main Program
l_map, movements = get_data("Input.txt")

for dir in movements:
    if dir == "^":
        l_map = move_robot_up(l_map)
    elif dir == "v":
        l_map = move_robot_down(l_map)
    elif dir == "<":
        l_map = move_robot_left(l_map)
    elif dir == ">":
        l_map = move_robot_right((l_map))
    else:
        print("Unknown direction", dir)

print("The score after the movements is:", calculate_score(l_map))


