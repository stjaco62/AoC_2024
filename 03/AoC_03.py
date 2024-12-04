import re
# Read the file
def read_file(filename):
    l_text = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            l_text.append(line)
    text = "".join(l_text)
    return text

def search_mul(text):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    l_muls = re.findall(pattern, text)
    return l_muls

def calc_muls(l_mul):
    sum_mul = 0
    for mul in l_mul:
        mul = mul.split(",")
        fac1 = int(mul[0][4:])
        fac2 = int(mul[1][:-1])
        sum_mul += fac1 * fac2
    return sum_mul

def split_text(text):
    l_text = []
    do = True
    while True:
        if do:
            text = text.split("don't()", maxsplit = 1)
            l_text.append(text[0])
        else:
            text = text.split("do()", maxsplit = 1)
        do = not(do)
        if len(text) == 2:
            text = text[1]
        else:
            break
    return l_text

# Main Program
text = read_file("Input.txt")
l_mul = []
l_mul += search_mul(text)
print(calc_muls(l_mul))

l_text = []
l_text += split_text(text)
l_mul = []
for t in l_text:
    l_mul += search_mul(t)
print(calc_muls(l_mul))
