from itertools import combinations

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

def get_antennas(l_map):
    d_antennas = {}
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col != ".":
                if col in d_antennas:
                    d_antennas[col].append((row_ind, col_ind))
                else:
                    d_antennas[col] = [(row_ind, col_ind)]
    return d_antennas

def get_antinode_pair(pair, max_ind):
    l_antinodes = []
    antenna1, antenna2 = pair
    row_diff = antenna2[0] - antenna1[0]
    col_diff = antenna2[1] - antenna1[1]
    if max_ind == -1:
        l_antinodes.append((antenna1[0] - row_diff, antenna1[1] - col_diff))
        l_antinodes.append((antenna2[0] + row_diff, antenna2[1] + col_diff))
        return l_antinodes
    else:
        for i in range(max_ind):
            l_antinodes.append((antenna1[0] - i * row_diff, antenna1[1] - i * col_diff))
            l_antinodes.append((antenna2[0] + i * row_diff, antenna2[1] + i * col_diff))
        return l_antinodes

def get_antinodes(l_antennas, max_ind):
    l_antinodes = []
    l_pairs = list(combinations(l_antennas, 2))
    for pair in l_pairs:
        l_antinodes += get_antinode_pair(pair, max_ind)
    return l_antinodes

def clean_list_antinodes(l_antinodes, max_row, max_col):
    new_list = []
    for antinode in l_antinodes:
        if 0 <= antinode[0] <= max_row and 0 <= antinode[1] <= max_col:
            new_list.append(antinode)
    return new_list

# Main Program
l_map = get_data("Input.txt")
d_antennas = get_antennas(l_map)
max_ind = max(len(l_map), len(l_map[0]))
l_antinodes = []
for antenna in d_antennas:
    l_antinodes += get_antinodes(d_antennas[antenna], -1)
clean_list = clean_list_antinodes(l_antinodes, len(l_map) - 1, len(l_map[0]) - 1)
clean_list = list(set(clean_list))
print(len(clean_list))
l_antinodes = []
for antenna in d_antennas:
    l_antinodes += get_antinodes(d_antennas[antenna], max_ind)
clean_list = clean_list_antinodes(l_antinodes, len(l_map) - 1, len(l_map[0]) - 1)
clean_list = list(set(clean_list))
print(len(clean_list))