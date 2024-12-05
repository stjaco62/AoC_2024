# Get Data
def get_data(filename):
    l_rules = []
    l_updates = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if "|" in line:
                line = line.split("|")
                l_rules.append(line)
            elif "," in line:
                line = line.split(",")
                l_updates.append(line)
    return l_rules, l_updates

def check_update(update, l_rules):
    for rule in l_rules:
        n1, n2 = rule
        if n1 in update and n2 in update:
            if update.index(n1) > update.index(n2):
                return 0
    return int(update[len(update) // 2])

def correct_update(update, l_rules):
    while True:
        swap = False
        for rule in l_rules:
            n1, n2 = rule
            if n1 in update and n2 in update:
                if update.index(n1) > update.index(n2):
                    ind1 = update.index(n1)
                    ind2 = update.index(n2)
                    update[ind1] = n2
                    update[ind2] = n1
                    swap = True
        if not(swap):
            break
    #print(update)
    return int(update[len(update) // 2])

def check_all_updates(l_updates, l_rules):
    sum_updates_correct = 0
    sum_updates_incorrect = 0
    for update in l_updates:
        x = check_update(update, l_rules)
        if x != 0:
            sum_updates_correct += x
        else:
            sum_updates_incorrect += correct_update(update, l_rules)
    return sum_updates_correct, sum_updates_incorrect

# Main Program
l_rules, l_updates = get_data("Input.txt")
print(check_all_updates(l_updates, l_rules))