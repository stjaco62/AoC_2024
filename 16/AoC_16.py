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

def make_dict_unvisited_nodes(l_map):
    max_dist = len(l_map) ** 3 * 1000
    d_unvisited_tile = {}
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            if col in [".", "E", "S"]:
                d_unvisited_tile[(row_ind, col_ind, 1, 0)] = max_dist
                d_unvisited_tile[(row_ind, col_ind, -1, 0)] = max_dist
                d_unvisited_tile[(row_ind, col_ind, 0, 1)] = max_dist
                d_unvisited_tile[(row_ind, col_ind, 0, -1)] = max_dist
    return d_unvisited_tile

def get_min_tile(d_tiles_unvisited):
    shortest_distance = min(d_tiles_unvisited.values())
    for tile, distance in d_tiles_unvisited.items():
        if distance == shortest_distance:
            return tile, distance

def find_path(l_map, start, l_targets):
    d_tiles_unvisited = make_dict_unvisited_nodes(l_map)
    d_tiles_visited = {}
    d_tiles_unvisited[start] = 0

    #while not(l_targets[0] in d_tiles_visited) and not(l_targets[1] in d_tiles_visited) and not(l_targets[2] in d_tiles_visited) and not(l_targets[3] in d_tiles_visited):
    while d_tiles_unvisited != {}:
        tile, distance = get_min_tile(d_tiles_unvisited)
        #print(tile, distance)
        del d_tiles_unvisited[tile]
        d_tiles_visited[tile] = distance
        if (tile[0] + tile[2], tile[1] + tile[3], tile[2], tile[3]) in d_tiles_unvisited:
            if d_tiles_unvisited[(tile[0] + tile[2], tile[1] + tile[3], tile[2], tile[3])] > d_tiles_visited[tile] + 1:
                d_tiles_unvisited[(tile[0] + tile[2], tile[1] + tile[3], tile[2], tile[3])] = d_tiles_visited[tile] + 1
        if tile[2] == 0:
            if (tile[0], tile[1], 1, 0) in d_tiles_unvisited and d_tiles_unvisited[(tile[0], tile[1], 1, 0)] > d_tiles_visited[tile] + 1000:
                d_tiles_unvisited[(tile[0], tile[1], 1, 0)] = d_tiles_visited[tile] + 1000
            if (tile[0], tile[1], -1, 0) in d_tiles_unvisited and d_tiles_unvisited[(tile[0], tile[1], -1, 0)] > d_tiles_visited[tile] + 1000:
                d_tiles_unvisited[(tile[0], tile[1], -1, 0)] = d_tiles_visited[tile] + 1000
        else:
            if (tile[0], tile[1], 0, 1) in d_tiles_unvisited and d_tiles_unvisited[(tile[0], tile[1], 0, 1)] > d_tiles_visited[tile] + 1000:
                d_tiles_unvisited[(tile[0], tile[1], 0, 1)] = d_tiles_visited[tile] + 1000
            if (tile[0], tile[1], 0, -1) in d_tiles_unvisited and d_tiles_unvisited[(tile[0], tile[1], 0, -1)] > d_tiles_visited[tile] + 1000:
                d_tiles_unvisited[(tile[0], tile[1], 0, -1)] = d_tiles_visited[tile] + 1000

    solutions = []
    for tile in l_targets:
        if tile in d_tiles_visited:
            print(tile, d_tiles_visited[tile])
            solutions.append(d_tiles_visited[tile])
    if solutions != []:
        return min(solutions), d_tiles_visited

    return -1
# Main Program
l_map = get_data("Input.txt")
pos_S, pos_E = find_S_E((l_map))
pos_R = (pos_S[0], pos_S[1], 0, 1)
l_targets = []
l_targets.append((pos_E[0], pos_E[1], 1, 0))
l_targets.append((pos_E[0], pos_E[1], -1, 0))
l_targets.append((pos_E[0], pos_E[1], 0, 1))
l_targets.append((pos_E[0], pos_E[1], 0, -1))

min_score, d_tiles_visited2 = find_path(l_map, pos_R, l_targets)
print("The shortest path has a score of", min_score, "points")

l_targets = []
l_targets.append((pos_S[0], pos_S[1], 0, 1))
pos_R = (pos_E[0], pos_E[1], 1, 0)

min_score2, d_tiles_visited1 = find_path(l_map, pos_R, l_targets)
print("The shortest path has a score of", min_score2, "points")

l_best_places = []
for row_ind, row in enumerate(l_map):
    for col_ind, col in enumerate(row):
        if col != "#":
            if d_tiles_visited1[(row_ind, col_ind, 1, 0)] + d_tiles_visited2[(row_ind, col_ind, -1, 0)] == min_score:
                l_best_places.append((row_ind, col_ind))
            if d_tiles_visited1[(row_ind, col_ind, -1, 0)] + d_tiles_visited2[(row_ind, col_ind, 1, 0)] == min_score:
                l_best_places.append((row_ind, col_ind))
            if d_tiles_visited1[(row_ind, col_ind, 0, 1)] + d_tiles_visited2[(row_ind, col_ind, 0, -1)] == min_score:
                l_best_places.append((row_ind, col_ind))
            if d_tiles_visited1[(row_ind, col_ind, 0, -1)] + d_tiles_visited2[(row_ind, col_ind, 0, 1)] == min_score:
                l_best_places.append((row_ind, col_ind))
l_best_places = list(set(l_best_places))
print("There are ", len(l_best_places), "best places")


