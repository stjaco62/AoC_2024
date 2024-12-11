def get_data(filename):
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
    return line

def blink_stone(stone):
    l_stones = []
    if stone == "0":
        l_stones.append("1")
    elif len(stone) % 2 == 0:
        l_stone = stone[:len(stone)//2]
        r_stone = stone[len(stone)//2:]
        r_stone = str(int(r_stone)) # remove leading 0s
        l_stones.append(l_stone)
        l_stones.append(r_stone)
    else:
        l_stones.append(str(int(stone) * 2024))
    return l_stones

def make_d_stones(l_stones):
    d_stones = {}
    for stone in l_stones:
        if stone in d_stones:
            d_stones[stone] += 1
        else:
            d_stones[stone] = 1
    return d_stones

def blink(d_stones):
    new_d_stones = {}
    for stone, num in d_stones.items():
        l_stones = blink_stone(stone)
        for stn in l_stones:
            if stn in new_d_stones:
                new_d_stones[stn] += num
            else:
                new_d_stones[stn] = num
    return new_d_stones

# Main Program
l_stones = get_data("Input.txt")
d_stones = make_d_stones((l_stones))

for _ in range(25):
    d_stones = blink(d_stones)
num_stones = 0
for stone, num in d_stones.items():
    num_stones += num
print(num_stones)

for _ in range(50):
    d_stones = blink(d_stones)
num_stones = 0
for stone, num in d_stones.items():
    num_stones += num
print(num_stones)