# Read Data from file
def read_data(file):
    l1 = []
    l2 = []
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            i1 = int(line[:5])
            i2 = int(line[8:])
            l1.append(i1)
            l2.append(i2)
    l1.sort()
    l2.sort()
    return l1, l2

# Go through lists and calculate the sum of differences
def sum_diff(l1, l2):
    s_diff = 0
    for i in range(len(l1)):
        diff = abs(l1[i] - l2[i])
        #print(l1[i], l2[i], diff)
        s_diff += diff
    return s_diff

# Go through l1, check for each element of l1 the counts in l2 ...
def sum_prod(l1, l2):
    s_prod = 0
    for i in l1:
        prod = i * l2.count(i)
        s_prod += prod
        #print(i, prod, s_prod)
    return s_prod

# Main Program
l1, l2 = read_data("Input_01.txt")
print(sum_diff(l1, l2))
print(sum_prod(l1, l2))