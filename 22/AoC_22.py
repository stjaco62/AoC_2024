def get_data(filename):
    l_secret_numbers = []
    with open(filename, "r") as file:
        for line in file:
            secret_number = int(line.strip())
            l_secret_numbers.append(secret_number)
    return l_secret_numbers

def mix_sn_num(sn, num):
    sn = sn ^ num
    return sn

def prune_sn(sn):
    sn = sn % 16777216
    return sn

def make_list_sn(sn):
    l_sn = [sn]
    for _ in range(2000):
        prod = sn * 64
        sn = mix_sn_num(sn, prod)
        sn = prune_sn(sn)
        result = sn // 32
        sn = mix_sn_num(sn, result)
        sn = prune_sn(sn)
        result = 2048 * sn
        sn = mix_sn_num(sn, result)
        sn = prune_sn(sn)
        l_sn.append(sn)
    return l_sn

def make_l_prices(l_sn):
    l_prices = []
    for sn in l_sn:
        l_prices.append(sn % 10)
    return l_prices

def make_l_changes(l_prices):
    l_changes = []
    for i in range(len(l_prices) - 1):
        l_changes.append(l_prices[i+1] - l_prices[i])
    return l_changes

def make_d_scores(l_prices, l_changes):
    d_scores = {}
    for i in range(len(l_changes) - 3):
        pattern = (l_changes[i], l_changes[i+1], l_changes[i+2], l_changes[i+3])
        if pattern not in d_scores:
            d_scores[pattern] = l_prices[i+4]
    return d_scores

# Main Program
l_sn = get_data("Input.txt")

#l_sn = [1, 2, 3, 2024]
total_scores = {}
sum_sn2000 = 0
for sn in l_sn:
    l_sn = make_list_sn(sn)
    sum_sn2000 += l_sn[-1]
    l_prices = make_l_prices(l_sn)
    l_changes = make_l_changes(l_prices)
    d_scores = make_d_scores(l_prices, l_changes)
    for pattern, score in d_scores.items():
        if pattern in total_scores:
            total_scores[pattern] += score
        else:
            total_scores[pattern] = score
print("Sum of secrets: ", sum_sn2000)
print("Max number of bananas: ", max(total_scores.values()))



