def get_data(filename):
    l_robots = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            pos, vel = line.split(" ")
            pos = pos.split("=")[1]
            pos = pos.split(",")
            pos = (int(pos[1]), int(pos[0]))
            vel = vel.split("=")[1]
            vel = vel.split(",")
            vel = (int(vel[1]), int(vel[0]))
            l_robots.append((pos, vel))
    return l_robots

def make_floor(num_rows, num_cols):
    l_map = []
    for row_ind in range(num_rows):
        row = []
        for col_ind in range(num_cols):
            row.append(0)
        l_map.append(row)
    return l_map

def print_map(l_map):
    for row in l_map:
        for col in row:
            if col == 0:
                print(".", end = "")
            else:
                print(col, end = "")
        print()

def position_robots(l_map, l_robots):
    for robot in l_robots:
        pos, vel = robot
        l_map[pos[0]][pos[1]] += 1
    return l_map

def move_robot(pos, vel, num_steps, max_row, max_col):
    pos, vel = robot
    pos_x, pos_y = pos
    vel_x, vel_y = vel
    new_pos_x = (pos_x + num_steps * vel_x) % max_row
    new_pos_y = (pos_y + num_steps * vel_y) % max_col
    return (new_pos_x, new_pos_y)

def sum_quadrant(map_quadrant):
    fac = 0
    for row in map_quadrant:
        for col in row:
            fac += col
    return fac

def calc_safetyfactor(l_robots, max_row, max_col):
    half_row = max_row // 2
    half_col = max_col // 2
    fac1 = 0
    fac2 = 0
    fac3 = 0
    fac4 = 0
    for robot in l_robots:
        pos, vel = robot
        if 0 <= pos[0] < half_row and 0 <= pos[1] < half_col:
            fac1 += 1
        elif 0 <= pos[0] < half_row and half_col + 1 <= pos[1] <= max_col:
            fac2 += 1
        elif half_row + 1 <= pos[0] < max_row and 0 <= pos[1] < half_col:
            fac3 += 1
        elif half_row + 1 <= pos[0] < max_row and half_col + 1 <= pos[1] <= max_col:
            fac4 += 1
    return fac1 * fac2 * fac3 * fac4

# Main Program
l_robots = get_data("Input.txt")
max_row = 103     # Test floor 7 * 11, real floor: 103 * 101
max_col = 101

l_new_robots = []
for robot in l_robots:
    pos, vel = robot
    new_pos = move_robot(pos, vel, 100, max_row, max_col)
    l_new_robots.append((new_pos, vel))
l_robots = l_new_robots

l_map = make_floor(max_row, max_col)
l_map = position_robots(l_map, l_robots)
print(calc_safetyfactor(l_robots, max_row, max_col))

l_robots = get_data("Input.txt")

l_sfactors = []

for i in range(7687):
    l_new_robots = []
    for robot in l_robots:
        pos, vel = robot
        new_pos = move_robot(pos, vel, 1, max_row, max_col)
        l_new_robots.append((new_pos, vel))
    l_robots = l_new_robots

    l_map = make_floor(max_row, max_col)
    l_map = position_robots(l_map, l_robots)
    l_sfactors.append(calc_safetyfactor(l_robots, max_row, max_col))

print(min(l_sfactors))
print(l_sfactors.index(min(l_sfactors)))

# Print the christmas tree
print_map(l_map)
