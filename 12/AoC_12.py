def get_data(filename):
    l_map = []
    with open(filename, "r") as file:
        for line in file:
            row = []
            line = line.strip()
            for char in line:
                row.append(char)
            l_map.append(row)
    return l_map

def is_in_map(l_map, pos):
    if 0 <= pos[0] <= len(l_map) - 1 and 0 <= pos[1] <= len(l_map[0]) - 1:
        return True
    return False

def find_region(l_map, region, pos):
    region.append(pos)
    l_diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for diff in l_diffs:
        new_pos = (pos[0] + diff[0], pos[1] + diff[1])
        if is_in_map(l_map, new_pos):
            if l_map[pos[0]][pos[1]] == l_map[new_pos[0]][new_pos[1]]:
                if not (new_pos in region):
                    find_region(l_map, region, new_pos)
    return region

def calculate_region(l_map, region):
    area = len(region)
    perimeter = 0
    l_diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for plant in region:
        for diff in l_diffs:
            if not(is_in_map(l_map, (plant[0] + diff[0], plant[1] + diff[1]))):
                perimeter += 1
            elif l_map[plant[0]][plant[1]] != l_map[plant[0] + diff[0]][plant[1] + diff[1]]:
                perimeter += 1
    return area * perimeter

def calculate_region2(l_map, region):
    # Search W --> E
    num_sides = 0
    l_sideplants_W = []
    l_sideplants_E = []
    l_sideplants_N = []
    l_sideplants_S = []
    for row_ind, row in enumerate(l_map):
        for col_ind, col in enumerate(row):
            pos = (row_ind, col_ind)
            pos_W = (row_ind, col_ind - 1)
            pos_E = (row_ind, col_ind + 1)
            pos_N = (row_ind - 1, col_ind)
            pos_S = (row_ind + 1, col_ind)
            if pos in region:
                if not (is_in_map(l_map, pos_W)) or l_map[pos[0]][pos[1]] != l_map[pos_W[0]][pos_W[1]]:
                    l_sideplants_W.append(pos)
                    if not (is_in_map(l_map, pos_N)) or not (pos_N in l_sideplants_W):
                        num_sides += 1
            if pos in region:
                if not (is_in_map(l_map, pos_E)) or l_map[pos[0]][pos[1]] != l_map[pos_E[0]][pos_E[1]]:
                    l_sideplants_E.append(pos)
                    if not (is_in_map(l_map, pos_N)) or not (pos_N in l_sideplants_E):
                        num_sides += 1
            if pos in region:
                if not (is_in_map(l_map, pos_N)) or l_map[pos[0]][pos[1]] != l_map[pos_N[0]][pos_N[1]]:
                    l_sideplants_N.append(pos)
                    if not (is_in_map(l_map, pos_W)) or not (pos_W in l_sideplants_N):
                        num_sides += 1
            if pos in region:
                if not (is_in_map(l_map, pos_S)) or l_map[pos[0]][pos[1]] != l_map[pos_S[0]][pos_N[1]]:
                    l_sideplants_S.append(pos)
                    if not (is_in_map(l_map, pos_W)) or not (pos_W in l_sideplants_S):
                        num_sides += 1

    return num_sides * len(region)











# Main Program
l_map = get_data("Test.txt")
l_plants = []
l_regions = []
for row_ind, row in enumerate(l_map):
    for col_ind, col in enumerate(row):
        if not((row_ind, col_ind) in l_plants):
            pos = (row_ind, col_ind)
            new_region = find_region(l_map, [], pos)
            l_regions.append(new_region)
            l_plants += new_region
total_price = 0
for region in l_regions:
    total_price += calculate_region(l_map, region)
print(total_price)

total_price = 0
for region in l_regions:
    total_price += calculate_region2(l_map, region)
    #print(l_map[region[0][0]][region[0][1]], num_sides)
print(total_price)



'''
for region in l_regions:
    print(l_map[region[0][0]][region[0][1]], region)

for row in l_map:
    for char in row:
        print(char, end = "")
    print()
'''