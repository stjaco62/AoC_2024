def get_data(filename):
    l_arcades = []
    with open(filename, "r") as file:
        while True:
            buttonA = file.readline().strip()
            buttonA = buttonA.split(": ")[1].split(", ")
            buttonA[0] = int(buttonA[0][2:])
            buttonA[1] = int(buttonA[1][2:])
            buttonB = file.readline().strip()
            buttonB = buttonB.split(": ")[1].split(", ")
            buttonB[0] = int(buttonB[0][2:])
            buttonB[1] = int(buttonB[1][2:])
            prize = file.readline().strip()
            prize = prize.split(": ")[1].split(", ")
            prize[0] = int(prize[0][2:])
            prize[1] = int(prize[1][2:])
            arcade = (buttonA, buttonB, prize)
            l_arcades.append(arcade)
            test = file.readline()
            if not test:
                break
    return l_arcades

def find_move(arcade):
    butA, butB, prize = arcade
    token = 10000
    for moveA in range(101):
        for moveB in range(101):
            if moveA * butA[0] + moveB * butB[0] == prize[0] and \
                    moveA * butA[1] + moveB * butB[1] == prize[1]:
                if moveA * 3 + moveB < token:
                    token = moveA * 3 + moveB
    if token == 10000:
        return 0
    else:
        return token

def add_prize(arcade):
    butA, butB, prize = arcade
    prize[0] += 10000000000000
    prize[1] += 10000000000000
    arcade = (butA, butB, prize)
    return arcade

def find_move2(arcade):
    butA, butB, prize = arcade
    det = butA[0] * butB[1] - butA[1] * butB[0]
    if det == 0:
        return 0
    detA = prize[0] * butB[1] - prize[1] * butB[0]
    detB = butA[0] * prize[1] - butA[1] * prize[0]
    moveA = detA // det
    moveB = detB // det

    if moveA * butA[0] + moveB * butB[0] == prize[0] and \
            moveA * butA[1] + moveB * butB[1] == prize[1]:
        return moveA * 3 + moveB
    else:
        return 0


# Main Program
l_arcades = get_data("Input.txt")
total_token = 0
for arcade in l_arcades:
    total_token += find_move(arcade)
print(total_token)

new_l_arcades = []
for arcade in l_arcades:
    new_l_arcades.append(add_prize(arcade))
l_arcades = new_l_arcades

total_token = 0
for arcade in l_arcades:
    total_token += find_move2(arcade)
print(total_token)
