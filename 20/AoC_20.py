def get_data(filename):
    l_map = []
    with open(filename, "r") as file:
        for line in file:
            row = []
            line = line.strip()
            for col in line:
                row.append(col)
            l_map.append(row)
    return l_map

def find_S_E(l_map):
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col == "S":
                pos_S = (row_ind, col_ind)
            if col == "E":
                pos_E = (row_ind, col_ind)
    return pos_S, pos_E

def make_dict_unvisited(l_map):
    d_pos = {}
    max_step = len(l_map) ** 3
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col in [".", "S", "E"]:
                d_pos[(row_ind, col_ind)] = max_step
    return d_pos

def find_min_pos(d_unv):
    min_steps = min(d_unv.values())
    for pos, steps in d_unv.items():
        if steps == min_steps:
            return pos, steps

def find_neighbours(l_map, d_unv, pos, steps_so_far):
    l_diff = [(1,0), (-1, 0), (0, 1), (0, -1)]
    for diff in l_diff:
        new_pos = (pos[0] + diff[0], pos[1] + diff[1])
        if l_map[pos[0] + diff[0]][pos[1] + diff[1]] != "#" and new_pos in d_unv:
            if d_unv[new_pos] > steps_so_far + 1:
                d_unv[new_pos] = steps_so_far + 1
    return d_unv

def find_path(l_map, start):
    d_unv = make_dict_unvisited(l_map)
    d_vis = {}
    d_unv[start] = 0

    while not d_unv == {}:
        pos, steps = find_min_pos(d_unv)
        del d_unv[pos]
        d_vis[pos] = steps
        d_unv = find_neighbours(l_map, d_unv, pos, d_vis[pos])

    return d_vis

def find_cheats(d_vis):
    l_cheats = []
    #l_diff = [(2, 0), (-2, 0), (0, 2), (0, -2), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    l_diff = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    for pos, steps in d_vis.items():
        for diff in l_diff:
            new_pos = (pos[0] + diff[0], pos[1] + diff[1])
            if new_pos in d_vis:
                if d_vis[new_pos] > steps + 2:
                    l_cheats.append((pos, new_pos, d_vis[new_pos] - steps - 2))
    return l_cheats

def find_big_cheats(d_vis):
    l_cheats = []
    l_diff = []
    for row in range(-20, 21):
        for col in range(-20, 21):
            if abs(row) + abs(col) <= 20:
                l_diff.append((row, col))
    for pos, steps in d_vis.items():
        for diff in l_diff:
            new_pos = (pos[0] + diff[0], pos[1] + diff[1])
            num_cheats = abs(diff[0]) + abs(diff[1])
            if new_pos in d_vis:
                if d_vis[new_pos] > steps + num_cheats:
                    l_cheats.append((pos, new_pos, d_vis[new_pos] - steps - num_cheats))
    return l_cheats

# Main Program
l_map = get_data("Input.txt")
pos_S, pos_E = find_S_E((l_map))       
d_vis = find_path(l_map, pos_S)
print("Minimum path:", d_vis[(pos_E)])
l_cheats = find_cheats(d_vis)
cheat_100 = 0
for cheat in l_cheats:
    if cheat[2] >= 100:
        cheat_100 += 1
print("There are",  cheat_100, "cheats which save over 100 steps")

l_big_cheats = find_big_cheats(d_vis)
cheat_100 = 0
for cheat in l_big_cheats:
    if cheat[2] >= 100:
        cheat_100 += 1
print("There are",  cheat_100, "big cheats which save over 100 steps")
