import re

part1_answer = 0
part2_answer = 0

with open("input.txt", "r") as input_file:
    do = True
    for input_line in input_file:
        matches = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', input_line)
        for match in matches:
            if match == "do()":
                do = True
                continue

            if match == "don't()":
                do = False
                continue

            num1, num2 = list(map(int, match[4:-1].split(",")))
            part1_answer += num1 * num2
            if do:
                part2_answer += num1 * num2

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
