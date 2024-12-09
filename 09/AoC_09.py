def get_data(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            disk_map = line
    return disk_map

def make_disk(disk_map):
    disk = []
    file_ID = 0
    empty = False
    for file_length in disk_map:
        file_length = int(file_length)
        for i in range(file_length):
            if not empty:
                disk.append(file_ID)
            else:
                disk.append(".")
        if not empty:
            file_ID += 1
        empty = not(empty)
    return disk

def compact_disk(disk,num_blocks):
    for block_ind, block in enumerate(disk):
        if block == ".":
            disk[block_ind] = disk[-1]
            del disk[-1]
            while disk[-1] == ".":
                del disk[-1]
    while len(disk) < num_blocks:
        disk.append(".")
    return disk

def calc_checksum(disk):
    pos = 0
    checksum = 0
    for block in disk:
        if block != ".":
            checksum += block * pos
        pos += 1
    return checksum

def make_disk2(disk_map):
    disk = []
    file_ID = 0
    empty = False
    for file_length in disk_map:
        if not empty:
            disk.append([file_ID, int(file_length)])
        else:
            disk.append([".", int(file_length)])
        if not empty:
            file_ID += 1
        empty = not empty
    return disk

def compact_disk2(disk):
    for ind_back in range(len(disk) - 1, - 1, - 1):
        if disk[ind_back][0] != ".":
            for ind_front in range(len(disk)):
                if ind_front >= ind_back:
                    break
                if disk[ind_front][0] == ".":
                    if disk[ind_front][1] >= disk[ind_back][1]:
                        x = disk[ind_back].copy()
                        disk[ind_back][0] = "."
                        disk.insert(ind_front, x)

                        disk[ind_front + 1][1] -= disk[ind_front][1]
                        break
 
    return disk

def make_disk3(disk):
    new_disk = []
    for file in disk:
        for i in range(file[1]):
            new_disk.append(file[0])
    return new_disk

# Main Program
disk_map = get_data("Input.txt")
disk = make_disk(disk_map)
disk = compact_disk(disk, len(disk))
print(calc_checksum(disk))
disk = make_disk2(disk_map)
disk = compact_disk2(disk)
disk = make_disk3(disk)
print(calc_checksum(disk))



