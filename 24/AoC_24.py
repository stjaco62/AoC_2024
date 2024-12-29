def get_data(filename):
    d_outputs = {}
    d_gates = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            gate, value = line.split(": ")
            d_outputs[gate] = bool(int(value))
        for line in file:
            line = line.strip()
            gate, node_out = line.split(" -> ")
            node_in1, operand, node_in2 = gate.split(" ")
            operand = operand.lower()
            gate = (node_in1, node_in2, operand)
            if not gate in d_gates:
                d_gates[gate] = [node_out]
            else:
                d_gates[gate].append(node_out)
    return d_outputs, d_gates

def calc_gates(d_gates, d_outputs):
    Ready = True
    for gate in d_gates:
        node_in1, node_in2, operand = gate
        if node_in1 in d_outputs and node_in2 in d_outputs:
            inp1 = d_outputs[node_in1]
            inp2 = d_outputs[node_in2]
            if operand == "and":
                for output_gate in d_gates[gate]:
                    d_outputs[output_gate] = inp1 and inp2
            elif operand == "or":
                for output_gate in d_gates[gate]:
                    d_outputs[output_gate] = inp1 or inp2
            elif operand == "xor":
                for output_gate in d_gates[gate]:
                    d_outputs[output_gate] = inp1 ^ inp2
            else:
                print("Unknown operator", operand)
        else:
            Ready = False
    return d_outputs, Ready

def calc_z_values(d_outputs):
    z = ""
    i = 0
    while True:
        if i < 10:
            gate = "z0" + str(i)
        else:
            gate = "z" + str(i)
        if gate in d_outputs:
            if d_outputs[gate]:
                z = "1" + z
            else:
                z = "0" + z
        else:
            break
        i += 1
    return int(z, 2)




# Main Program
d_outputs, d_gates = get_data("Input.txt")
# Repair
d_gates[("y14", "x14", "and")] = ["vhm"]
d_gates[("ndq", "rkm", "xor")] = ["z14"]
d_gates[("snv", "jgq", "or")] = ["mps"]
d_gates[("kqw", "kqj", "xor")] = ["z27"]
d_gates[("trn","gpm", "and")] = ["msq"]
d_gates[("gpm", "trn", "xor")] = ["z39"]
d_gates[("x09", "x09", "xor")] = ["cnk"]
d_gates[("x09", "y09", "and")] = ["qwf"]
num_bits = 45

for x_bit in range(num_bits):
    d_outputs = {}
    for i in range(num_bits):
        if i < 10:
            d_outputs["x0" + str(i)] = bool(0)
            d_outputs["y0" + str(i)] = bool(0)
        else:
            d_outputs["x" + str(i)] = bool(0)
            d_outputs["y" + str(i)] = bool(0)
    if x_bit < 10:
        d_outputs["x0" + str(x_bit)] = True
        #d_outputs["y0" + str(x_bit)] = True
    else:
        d_outputs["x" + str(x_bit)] = True
        #d_outputs["y" + str(x_bit)] = True


    while True:
        d_outputs, Ready = calc_gates(d_gates, d_outputs)
        if Ready:
            break
    #print(calc_z_values(d_outputs))

    x = ""
    y = ""
    z = ""
    for i in range(num_bits):
        if i < 10:
            if "x0" + str(i) in d_outputs:
                x = str(int(d_outputs["x0" + str(i)])) + x
            if "y0" + str(i) in d_outputs:
                y = str(int(d_outputs["y0" + str(i)])) + y
            if "z0" + str(i) in d_outputs:
                z = str(int(d_outputs["z0" + str(i)])) + z
        else:
            if "x" + str(i) in d_outputs:
                x = str(int(d_outputs["x" + str(i)])) + x
            if "y" + str(i) in d_outputs:
                y = str(int(d_outputs["y" + str(i)])) + y
            if "z" + str(i) in d_outputs:
                z = str(int(d_outputs["z" + str(i)])) + z
        if i % 4 == 3:
            x = " " + x
            y = " " + y
            z = " " + z
    if num_bits < 10:
        if "z0" + str(num_bits) in d_outputs:
            z = str(int(d_outputs["z0" + str(num_bits)])) + z
        elif "z" + str(num_bits) in d_outputs:
            z = str(int(d_outputs["z" + str(num_bits)])) + z

    print("X: ", x)
    print("Y: ", y)
    print("Z: ", z)
    print()


print(",".join(sorted(["vhm", "z14", "mps", "z27", "msq", "z39", "cnk", "qwf"])))
#for node, output in d_gates.items():
#    print(node, output)