
from functools import cache

def get_data(filename):
    l_codes = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            l_codes.append(line)
    return l_codes

def create_numkey_graph():
    d_pos = {}
    d_pos["7"] = (0, 0)
    d_pos["8"] = (0, 1)
    d_pos["9"] = (0, 2)
    d_pos["4"] = (1, 0)
    d_pos["5"] = (1, 1)
    d_pos["6"] = (1, 2)
    d_pos["1"] = (2, 0)
    d_pos["2"] = (2, 1)
    d_pos["3"] = (2, 2)
    d_pos["0"] = (3, 1)
    d_pos["A"] = (3, 2)
    graph = {}
    for x, (x1, x2) in d_pos.items():
        for y, (y1, y2) in d_pos.items():
            path = '<' * (x2 - y2) + 'v' * (y1 - x1) + '^' * (x1 - y1) + '>' * (y2 - x2)
            if (3, 0) == (x1, y2) or (3, 0) == (y1, x2):
                path = path[::-1]
            graph[(x, y)] = path + 'A'
    return graph

def create_dirkey_graph():
    d_pos = {}
    d_pos["^"] = (0, 1)
    d_pos["A"] = (0, 2)
    d_pos["<"] = (1, 0)
    d_pos["v"] = (1, 1)
    d_pos[">"] = (1, 2)
    graph = {}
    for x, (x1, x2) in d_pos.items():
        for y, (y1, y2) in d_pos.items():
            path = '<' * (x2 - y2) + 'v' * (y1 - x1) + '^' * (x1 - y1) + '>' * (y2 - x2)
            if (0, 0) == (x1, y2) or (0, 0) == (x2, y1):
                path = path[::-1]
            graph[(x, y)] = path + 'A'
    return graph

def get_dirs(code, num_graph):
    code = "A" + code
    dirs = ""
    for i in range(len(code) - 1):
        dirs += num_graph[(code[i], code[i + 1])]
    return dirs

@cache
def get_length(dirs, iterations):
    global dir_graph
    if iterations == 0:
        return len(dirs)
    dirs = "A" + dirs
    total_length = 0
    for i in range(len(dirs) - 1):
        total_length += get_length(dir_graph[(dirs[i], dirs[i + 1])], iterations - 1)
    return total_length

# Main Program
l_code = get_data("Input.txt")

num_graph = create_numkey_graph()
dir_graph = create_dirkey_graph()

complexity = 0
for code in l_code:
    dirs = get_dirs(code, num_graph)
    complexity += get_length(dirs, 2) * int(code[:-1])
print("Part 1: ", complexity)

complexity = 0
for code in l_code:
    dirs = get_dirs(code, num_graph)
    complexity += get_length(dirs, 25) * int(code[:-1])
print("Part 2: ", complexity)
