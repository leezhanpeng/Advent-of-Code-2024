part1_answer = 0
part2_answer = 0

right_list, left_list = [], []
left_list_occurrences = {}

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        right_number, left_number = list(map(int, input_line.strip().split("   ")))
        
        right_list.append(right_number)
        left_list.append(left_number)

        left_list_occurrences[left_number] = left_list_occurrences.get(left_number, 0) + 1
    
right_list.sort()
left_list.sort()

for right_number, left_number in zip(right_list, left_list):
    part1_answer += abs(right_number - left_number)
    part2_answer += right_number * left_list_occurrences.get(right_number, 0)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
