# Get Data
def get_data(filename):
    l_map = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            row = []
            for char in line:
                row.append(char)
            l_map.append(row)
    return l_map

def find_guard(l_map):
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col in ["^", ">", "<", "v"]:
                return row_ind, col_ind, col
    return "Guard not found"

def move_guard_one_step(l_map, guard_pos):
    row, col, drct = guard_pos
    l_map[row][col] = "X"
    if drct == "^":
        if row - 1 < 0:
            return -1
        elif l_map[row - 1][col] == "#":
            return row, col, ">"
        else:
            return row - 1, col, "^"
    elif drct == ">":
        if col + 1 == len(l_map[0]):
            return -1
        elif l_map[row][col + 1] == "#":
            return row, col, "v"
        else:
            return row, col + 1, ">"
    elif drct == "v":
        if row + 1 == len(l_map):
            return -1
        elif l_map[row + 1][col] == "#":
            return row, col, "<"
        else:
            return row + 1, col, "v"
    elif drct == "<":
        if col - 1 < 0:
            return -1
        elif l_map[row][col - 1] == "#":
            return row, col, "^"
        else:
            return row, col - 1, "<"
    else:
        return "Something went wrong"

def walk_guard(l_map, guard_pos):
    l_pos = [guard_pos]
    while True:
        guard_pos = move_guard_one_step(l_map, guard_pos)
        if guard_pos in l_pos:
            return "found loop", l_map
        l_pos.append(guard_pos)
        if guard_pos == -1:
            return "out of map", l_map

def count_steps(l_map):
    steps = 0
    for row in l_map:
        for col in row:
            if col == "X":
                steps += 1
    return steps

def print_map(l_map2):
    for row in l_map2:
       for col in row:
           print(col, end = "")
       print()

def set_obstacle_and_try(guard_pos, row_ind, col_ind):
    print(row_ind, col_ind)
    new_map = get_data("Input.txt")
    new_map[row_ind][col_ind] = "#"
    result, new_map = walk_guard(new_map, guard_pos)
    return result



# Main Program
l_map_initial = get_data("Input.txt")
l_map = l_map_initial.copy()
guard_pos = find_guard(l_map)
result, l_map = walk_guard(l_map, guard_pos)
print(count_steps(l_map))
loops = 0
for row_ind in range(len(l_map)):
    for col_ind in range(len(l_map[0])):
        if set_obstacle_and_try(guard_pos, row_ind, col_ind) == "found loop":
            loops += 1
print(loops)



