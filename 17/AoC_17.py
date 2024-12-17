def read_data(filename):
    d_reg = {}
    prog = []
    with open(filename, "r") as file:
        for _ in range(3):
            line = file.readline()
            line = line.strip()
            line = line.split(": ")
            reg_name = line[0][-1]
            reg_cont = int(line[1])
            d_reg[reg_name] = reg_cont
        line = file.readline()
        line = file.readline()
        line = line.split(": ")[1].split(",")
        for instr in line:
            prog.append(int(instr))
    return d_reg, prog

def combo_operand(operand, d_reg):
    if operand == 4:
        operand = d_reg["A"]
    elif operand == 5:
        operand = d_reg["B"]
    elif operand == 6:
        operand = d_reg["C"]
    return operand




def run_prog(prog, d_reg):
    output = []
    instr_pnt = 0
    while True:
        instr = prog[instr_pnt]
        operand = prog[instr_pnt + 1]
        if instr == 0:
            operand = combo_operand(operand, d_reg)
            d_reg["A"] = d_reg["A"] // (2 ** operand)
        elif instr == 1:
            d_reg["B"] = d_reg["B"] ^ operand
        elif instr == 2:
            operand = combo_operand(operand, d_reg)
            d_reg["B"] = operand % 8
        elif instr == 3:
            if d_reg["A"] == 0:
                pass
            else:
                instr_pnt = operand - 2
        elif instr == 4:
            d_reg["B"] = d_reg["B"] ^ d_reg["C"]
        elif instr == 5:
            operand = combo_operand(operand, d_reg)
            operand %= 8
            output.append(operand)
        elif instr == 6:
            operand = combo_operand(operand, d_reg)
            d_reg["B"] = d_reg["A"] // (2 ** operand)
        elif instr == 7:
            operand = combo_operand(operand, d_reg)
            d_reg["C"] = d_reg["A"] // (2 ** operand)
        else:
            print("Unknown instruction")
            break

        instr_pnt += 2
        if instr_pnt >= len(prog):
            #print(d_reg)
            #print(output)
            break
    return output









# Main Program
d_reg, prog = read_data("Input.txt")
print (d_reg)
print(prog)
#d_reg = {"A": 117440, "B": 0, "C": 0}
#prog = [0, 3, 5, 4, 3, 0]

A = 35184372088832 + 32 * 4398046511104 +  24 * 549755813888 + 16 * 68719476736 + 16 * 8589934592 + \
    24 * 1073741824 + 40 * 134217728 + 1 * 16777216 + 3 * 2097152 + 4 * 262144

while True:
    d_reg["A"] = A
    output = run_prog(prog, d_reg)
    if prog == output:
        print(output)
        print(A)
        break
    if A % 10000 == 0:
        print(A)
    A += 1
