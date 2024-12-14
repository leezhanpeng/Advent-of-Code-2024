import re

part1_answer = 0
part2_answer = 0

def count_presses(a1, b1, c1, a2, b2, c2):
    # Simultaneous equation
    # a1*x + b1*y = c1
    # a2*x + b2*y = c2
    y = (c2 * a1 - b1 * c1) / (b2 * a1 - b1 * a2)
    x = (c1 - a2 * y) / a1
    if (x >= 0 and x == int(x) and
        y >= 0 and y == int(y)):
        return int(x * 3 + y)
    return 0

with open("input.txt", "r") as input_file:
    machines = [{}]
    for input_line in input_file:
        if input_line.strip() == "":
            machines.append({})
        elif "button_a" not in machines[-1]:
            machines[-1]["button_a"] = list(map(int, re.findall(r"\+(\d+)", input_line)))
        elif "button_b" not in machines[-1]:
            machines[-1]["button_b"] = list(map(int, re.findall(r"\+(\d+)", input_line)))
        else:
            machines[-1]["goal"] = list(map(int, re.findall(r"\=(\d+)", input_line)))

for machine in machines:
    goal, button_a, button_b = machine["goal"], machine["button_a"], machine["button_b"]
    part1_answer += count_presses(button_a[0], button_a[1], goal[0], button_b[0], button_b[1], goal[1])
    part2_answer += count_presses(button_a[0], button_a[1], goal[0]+10000000000000, button_b[0], button_b[1], goal[1]+10000000000000)
  
print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
