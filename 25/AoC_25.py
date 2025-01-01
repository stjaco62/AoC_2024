def get_data(filename):
    l_locks = []
    l_keys = []
    with open(filename, "r") as file:
        while True:
            l_lines = []
            for l in range(7):
                line = file.readline()
                line = line.strip()
                if l == 0:
                    if line == "#####":
                        pattern = "lock"
                    else:
                        pattern = "key"
                l_lines.append(line)
            l_pins = [-1, -1, -1, -1, -1]
            for row_ind, row in enumerate(l_lines):
                for col_ind, chr in enumerate(row):
                    if chr == "#":
                        l_pins[col_ind] += 1
            if pattern == "key":
                l_keys.append(l_pins)
            else:
                l_locks.append(l_pins)
            line = file.readline()
            if line == "":
                break
    return l_keys, l_locks

def key_fits_lock(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

# Main Program
l_keys, l_locks = get_data("Input.txt")
num_fits = 0
for key in l_keys:
    for lock in l_locks:
        if key_fits_lock(key, lock):
            num_fits += 1
print("The number of fitting combinations is:", num_fits)






