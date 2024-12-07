from typing import List

part1_answer = 0
part2_answer = 0

def is_solvable(test_value: int, numbers: List[int], current_aggregation: int = 0, index: int = 0, include_concat: bool = False):
    if index == len(numbers):
        return test_value == current_aggregation

    if current_aggregation == 0:
        return is_solvable(test_value, numbers, current_aggregation=numbers[0], index=1, include_concat=include_concat)

    solvable = (is_solvable(test_value, numbers, current_aggregation=current_aggregation+numbers[index], index=index+1, include_concat=include_concat) or 
                is_solvable(test_value, numbers, current_aggregation=current_aggregation*numbers[index], index=index+1, include_concat=include_concat))
    
    if not solvable and include_concat:
        solvable = is_solvable(test_value, numbers, current_aggregation=int(str(current_aggregation)+str(numbers[index])), index=index+1, include_concat=include_concat)
    
    return solvable

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        test_value_string, numbers_string = input_line.strip().split(": ")
        test_value = int(test_value_string)
        numbers = list(map(int, numbers_string.split(" ")))
        if is_solvable(test_value, numbers):
            part1_answer += test_value
        if is_solvable(test_value, numbers, include_concat=True):
            part2_answer += test_value


print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
