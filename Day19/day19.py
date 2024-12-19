part1_answer = 0
part2_answer = 0

towels = set()
def num_possibilities(pattern: str, tracker: set = {}):
    if len(pattern) == 0:
        return 1

    if pattern in tracker:
        return tracker[pattern]

    total_count = 0
    for towel in towels:
        if pattern.startswith(towel):
            total_count += num_possibilities(pattern[len(towel):])

    tracker[pattern] = total_count
    return total_count

with open("input.txt", "r") as input_file:
    towels = set(next(input_file).strip().split(", "))
    next(input_file) # Whitespace
    for input_line in input_file:
        num_combinations = num_possibilities(input_line.strip())
        part1_answer += 1 if num_combinations else 0 
        part2_answer += num_combinations

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
