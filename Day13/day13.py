import re

part1_answer = 0
part2_answer = 0
    
with open("input.txt", "r") as input_file:
    machines = [{}]
    for input_line in input_file:
        if input_line.strip() == "":
            machines.append({})
        elif "button_a" not in machines[-1]:
            machines[-1]["button_a"] = list(map(lambda num: int(num[1:]), re.findall(r"\+\d+", input_line)))
        elif "button_b" not in machines[-1]:
            machines[-1]["button_b"] = list(map(lambda num: int(num[1:]), re.findall(r"\+\d+", input_line)))
        else:
            machines[-1]["goal"] = list(map(lambda num: int(num[1:]), re.findall(r"\=\d+", input_line)))

for machine in machines:
    goal, button_a, button_b = machine["goal"], machine["button_a"], machine["button_b"]
    # Simultaneous Equation: 2 Variables, 2 Equations
    push_B_count = (goal[1] * button_a[0] - button_a[1] * goal[0]) / (button_b[1] * button_a[0] - button_a[1] * button_b[0])
    push_A_count = (goal[0] - button_b[0] * push_B_count) / button_a[0]
    if (push_A_count >= 0 and push_A_count == int(push_A_count) and
        push_B_count >= 0 and push_B_count == int(push_B_count)):
        part1_answer += int(push_A_count * 3 + push_B_count)

    goal[0] += 10000000000000
    goal[1] += 10000000000000
    # Simultaneous Equation: 2 Variables, 2 Equations
    push_B_count = (goal[1] * button_a[0] - button_a[1] * goal[0]) / (button_b[1] * button_a[0] - button_a[1] * button_b[0])
    push_A_count = (goal[0] - button_b[0] * push_B_count) / button_a[0]
    if (push_A_count >= 0 and push_A_count == int(push_A_count) and
        push_B_count >= 0 and push_B_count == int(push_B_count)):
        part2_answer += int(push_A_count * 3 + push_B_count)
  
print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
