part1_answer = 0
part2_answer = 0

rules = {}
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        if "|" in input_line:
            before, after = list(map(int, input_line.strip().split("|")))
            rules[before] = rules.get(before, set())
            rules[before].add(after)
        elif input_line.strip() == "":
            continue
        else:
            numbers = list(map(int, input_line.strip().split(",")))
            is_correct = True

            visited = set()
            for index in range(len(numbers)):
                number = numbers[index]
                rule = rules.get(number, set())
                if len(rule.intersection(visited)) != 0:
                    is_correct = False
                    for sub_index in range(len(numbers)):
                        if numbers[sub_index] in rule:
                            numbers = numbers[:sub_index] + [numbers[index]] + numbers[sub_index:index] + numbers[index + 1:]
                            break
                visited.add(number)

            if is_correct:
                part1_answer += numbers[len(numbers) // 2]
            else:
                part2_answer += numbers[len(numbers) // 2]

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
