# Get Data
def get_data(filename):
    l_xmas = []
    with open(filename, "r") as file:
        for line in file:
            l_char = []
            line = line.strip()
            for char in line:
                l_char.append(char)
            l_xmas.append(l_char)
    return l_xmas

def make_border(l_xmas):
    for line in l_xmas:
        for _ in range(3):
            line.insert(0, ".")
            line.append(".")
    num_cols = len(l_xmas[0])
    new_line = []
    for i in range(num_cols):
        new_line.append(".")
    for _ in range(3):
        l_xmas.insert(0, new_line)
        l_xmas.append(new_line)
    return l_xmas

def search_xmas(l_xmas, row, col):
    score = 0
    for r_ind in range(-1, 2):
        for c_ind in range(-1, 2):
            word = ""
            for i in range(4):
                word += l_xmas[row + r_ind * i][col + c_ind * i]
            if word == "XMAS":
                score += 1
    return score

def search_x_mas(l_xmas, row, col):
    word1 = l_xmas[row - 1][col - 1] + l_xmas[row][col] + l_xmas[row + 1][col + 1]
    word2 = l_xmas[row + 1][col - 1] + l_xmas[row][col] + l_xmas[row - 1][col + 1]
    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
        return 1
    else:
        return 0

def search_matrix(l_xmas, fnct):
    num_row = len(l_xmas)
    num_col = len(l_xmas[0])
    score = 0
    for row in range(3, num_row - 3):
        for col in range(3, num_col - 3):
            score += fnct(l_xmas, row, col)
    return score

# Main Program
l_xmas = get_data("Input.txt")
l_xmas = make_border(l_xmas)
print(search_matrix(l_xmas, search_xmas))
print(search_matrix(l_xmas, search_x_mas))




