def get_data(filename):
    l_byte = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(",")
            pos_x = int(line[0])
            pos_y = int(line[1])
            l_byte.append((pos_x, pos_y))
    return l_byte

def make_map(l_byte, length, max_byte):
    l_map = []
    for row_ind in range(length):
        row = []
        for col_ind in range(length):
            row.append(".")
        l_map.append(row)
    num_bytes = 0
    for byte in l_byte:
        num_bytes += 1
        if num_bytes > max_byte:
            return l_map
        row_ind, col_ind = byte
        l_map[col_ind][row_ind] = "#"
    return l_map

def make_dict_unvisited_nodes(l_map):
    max_dist = len(l_map) ** 3
    d_unvisited_byte = {}
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if l_map[row_ind][col_ind] == ".":
                d_unvisited_byte[(row_ind, col_ind)] = max_dist
    return d_unvisited_byte

def get_min_byte(d_bytes_unvisited):
    shortest_distance = min(d_bytes_unvisited.values())
    for byte, distance in d_bytes_unvisited.items():
        if distance == shortest_distance:
            return byte, distance

def find_way(l_map, start, target):
    d_bytes_unvisited = make_dict_unvisited_nodes(l_map)
    d_bytes_visited = {}
    d_bytes_unvisited[start] = 0
    l_diff = [(1, 0), (-1, 0), (0, 1), (0,-1)]

    while not(target in d_bytes_visited):
        byte, distance = get_min_byte(d_bytes_unvisited)
        del d_bytes_unvisited[byte]
        d_bytes_visited[byte] = distance
        for diff in l_diff:
            if (byte[0] + diff[0], byte[1] + diff[1]) in d_bytes_unvisited:
                if d_bytes_unvisited[(byte[0] + diff[0], byte[1] + diff[1])] > distance + 1:
                    d_bytes_unvisited[(byte[0] + diff[0], byte[1] + diff[1])] = distance + 1

    return d_bytes_visited[target]

# Main Program
length = 71
max_byte = 1024
target = (length - 1, length - 1)
l_byte = get_data("Input.txt")
l_map = make_map(l_byte, length, max_byte)

print("Steps required:", find_way(l_map, (0,0), target))

max_byte = 2950 # To save some time
while True:
    l_map = make_map(l_byte, length, max_byte)
    num_steps = find_way(l_map, (0,0), target)
    if num_steps == length ** 3:
        print("Failed, last byte fallen:", l_byte[max_byte - 1])
        break
    max_byte += 1