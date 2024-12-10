def get_data(filename):
    l_map = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            row = []
            for char in line:
                row.append(int(char))
            l_map.append(row)
    return l_map

def get_trailheads(l_map):
    l_trailheads = []
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col == 0:
                l_trailheads.append((row_ind, col_ind))
    return l_trailheads

def search_trail(l_map, pos_row, pos_col, max_row, max_col):
    if l_map[pos_row][pos_col] == 9:
        return [(pos_row, pos_col)]
    num_trails = []
    for diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        row_diff, col_diff = diff
        if 0 <= pos_row + row_diff < max_row and 0 <= pos_col + col_diff < max_col:
            if l_map[pos_row + row_diff][pos_col + col_diff] == l_map[pos_row][pos_col] + 1:
                num_trails += search_trail(l_map, pos_row + row_diff, pos_col + col_diff, max_row, max_col)
    return num_trails

def search_trail2(l_map, pos_row, pos_col, max_row, max_col):
    if l_map[pos_row][pos_col] == 9:
        return 1
    num_trails = 0
    for diff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        row_diff, col_diff = diff
        if 0 <= pos_row + row_diff < max_row and 0 <= pos_col + col_diff < max_col:
            if l_map[pos_row + row_diff][pos_col + col_diff] == l_map[pos_row][pos_col] + 1:
                num_trails += search_trail2(l_map, pos_row + row_diff, pos_col + col_diff, max_row, max_col)
    return num_trails

# Main Program
l_map = get_data("Input.txt")
l_trailheads = get_trailheads(l_map)
max_row = len(l_map)
max_col = len(l_map[0])

num_trails = 0
for trailhead in l_trailheads:
    l_9pos = search_trail(l_map, trailhead[0], trailhead[1], max_row, max_col)
    l_9pos = list(set(l_9pos))
    num_trails += len(l_9pos)
print("Task1:", num_trails)

num_trails = 0
for trailhead in l_trailheads:
    num_trails += search_trail2(l_map, trailhead[0], trailhead[1], max_row, max_col)
print("Task2:", num_trails)




'''
for row in l_map:
    for num in row:
        print(num, end = "")
    print()
print(l_trailheads)
'''