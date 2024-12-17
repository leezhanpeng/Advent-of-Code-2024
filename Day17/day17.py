part1_answer = ""
part2_answer = 0

state = {}
with open("input.txt", "r") as input_file:
    initial_A = int(next(input_file).strip().split(": ")[1])
    initial_B = int(next(input_file).strip().split(": ")[1])
    initial_C = int(next(input_file).strip().split(": ")[1])
    state["A"] = initial_A
    state["B"] = initial_B
    state["C"] = initial_C
    next(input_file) # Whitespace
    program_string = next(input_file).strip().split(": ")[1]
    program = list(map(int, program_string.split(",")))

def get_operand_value(state, operand):
    if operand == 4:
        return state["A"]
    if operand == 5:
        return state["B"]
    if operand == 6:
        return state["C"]
    return operand

# Opcode 0
def adv(state, operand, program_index):
    state["A"] = int(state["A"] / 2**get_operand_value(state, operand))
    return program_index + 2

# Opcode 1
def bxl(state, operand, program_index):
    state["B"] = state["B"] ^ operand
    return program_index + 2

# Opcode 2
def bst(state, operand, program_index):
    state["B"] = get_operand_value(state, operand) % 8
    return program_index + 2

# Opcode 3
def jnz(state, operand, program_index):
    if state["A"] == 0:
        return program_index + 2
    return operand

# Opcode 4
def bxc(state, operand, program_index):
    state["B"] = state["B"] ^ state["C"]
    return program_index + 2

# Opcode 5
def out(state, operand, program_index):
    global output
    output += str(get_operand_value(state, operand) % 8)
    return program_index + 2

# Opcode 6
def bdv(state, operand, program_index):
    state["B"] = int(state["A"] / 2**get_operand_value(state, operand))
    return program_index + 2

# Opcode 7
def cdv(state, operand, program_index):
    state["C"] = int(state["A"] / 2**get_operand_value(state, operand))
    return program_index + 2

instructions = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv,
}

output = ""
program_index = 0
while program_index < len(program) - 1:
    opcode, operand = program[program_index], program[program_index + 1]
    program_index = instructions[opcode](state, operand, program_index)

part1_answer = ",".join(list(output))

program_output = ""
potential_A = -1
while program_output != program_string:
    potential_A += 1
    print(potential_A)
    state["A"] = potential_A
    state["B"] = initial_B
    state["C"] = initial_C

    output = ""
    program_index = 0
    while program_index < len(program) - 1:
        opcode, operand = program[program_index], program[program_index + 1]
        program_index = instructions[opcode](state, operand, program_index)
        program_output = ",".join(list(output))

part2_answer = potential_A # Brute force, won't work

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
