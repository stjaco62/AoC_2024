from functools import cache

def get_data(filename):
    l_towels = []
    l_patterns = []
    with open(filename, "r") as file:
        line = file.readline()
        line = line.strip()
        l_towels = line.split(", ")
        line = file.readline()
        for line in file:
            line = line.strip()
            l_patterns.append(line)
    return tuple(l_towels), l_patterns

@cache
def build_pattern(pattern, t_towels):
    build_possible = False
    for towel in t_towels:
        if pattern.startswith(towel):
            new_pattern = pattern[len(towel):]
            if new_pattern == "":
                return True
            else:
                build_possible = build_possible or build_pattern(new_pattern, t_towels)
    return build_possible

@cache
def build_pattern2(pattern, t_towels):
    arrangements = 0
    for towel in t_towels:
        if pattern.startswith(towel):
            new_pattern = pattern[len(towel):]
            if new_pattern == "":
                arrangements += 1
            else:
                arrangements += build_pattern2(new_pattern, t_towels)
    return arrangements

# Main Program
t_towels, l_patterns = get_data("Input.txt")

found_patterns = 0
for pattern in l_patterns:
    if build_pattern(pattern, t_towels):
        found_patterns += 1
print(found_patterns, "patterns found.")

arrangements = 0
for pattern in l_patterns:
    arrangements  += build_pattern2(pattern, t_towels)
print("There are ", arrangements, "arrangements")

