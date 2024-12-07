def get_data(filename):
    l_equations = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            result, l_nums = line.split(": ")
            result = int(result)
            l_nums = l_nums.split(" ")
            l_nums2 = []
            for num in l_nums:
                l_nums2.append(int(num))
            l_equations.append((result, l_nums2))
    return l_equations

def do_calculation(l_intermediate_results, l_nums, concat):
    if l_nums == []:
        return l_intermediate_results
    else:
        l_new_intermediateresults = []
        for num in l_intermediate_results:
            l_new_intermediateresults.append(num + l_nums[0])
            l_new_intermediateresults.append(num * l_nums[0])
            if concat:
                num_concat = int(str(num) + str(l_nums[0]))
                l_new_intermediateresults.append(num_concat)

        l_testresults = do_calculation(l_new_intermediateresults, l_nums[1:], concat)
        return l_testresults


def test_equation(equation, concat):
    result, l_nums = equation
    l_testresults = do_calculation([l_nums[0]], l_nums[1:], concat)
    if result in l_testresults:
        return result
    else:
        return 0

# Main Program
l_equations = get_data("Input.txt")
total = 0
for equation in l_equations:
    total += (test_equation(equation, concat = False))
print(total)
total = 0
for equation in l_equations:
    total += (test_equation(equation, concat = True))
print(total)




#for equation in l_equations:
#    print(equation)