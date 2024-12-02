part1_answer = 0
part2_answer = 0

def is_good_level(front_number: int, back_number: int, is_ascending: bool) -> bool:
    return 1 <= abs(front_number - back_number) <= 3 and (front_number < back_number) == is_ascending

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        report_numbers = list(map(int, input_line.strip().split(" ")))

        # To determine if the sequence is expected to increase or decrease, checking first 5 numbers is sufficient
        # If cannot be determined, then its unsafe lol
        num_ascending_pairs = 0
        num_descending_pairs = 0
        for index in range(4):
            front_number, back_number = report_numbers[index:index+2]
            num_ascending_pairs += front_number < back_number
            num_descending_pairs += front_number > back_number
        if num_ascending_pairs == num_descending_pairs:
            continue
        is_ascending = num_ascending_pairs > num_descending_pairs

        bad_level_indices = []
        for index in range(len(report_numbers) - 1):
            front_number, back_number = report_numbers[index:index+2]

            # Check for bad level
            if not is_good_level(front_number, back_number, is_ascending):
                bad_level_indices.append(index)

            # For sure unsafe
            if len(bad_level_indices) >= 3:
                break

        # Two bad levels that are not sequential is for sure unsafe, checking here to spare myself trouble when considering edge cases later
        if len(bad_level_indices) == 2 and bad_level_indices[1] - bad_level_indices[0] != 1:
            continue

        # Safe
        if len(bad_level_indices) == 0:
            part1_answer += 1
            part2_answer += 1
            continue

        # If the bad level is in the middle of the numbers, we need to bridge the gap and check if it is safe.
        # Else it is surely safe, since we are either removing the head or tail of the numbers.
        if len(bad_level_indices) == 1:
            bad_index = bad_level_indices[0]

            if bad_index == 0 or bad_index == len(report_numbers) - 2:
                part2_answer += 1
            else:
                front_good_number, front_bad_number, back_bad_number, back_good_number = report_numbers[bad_index-1:bad_index+3]
                part2_answer += is_good_level(front_good_number, back_bad_number, is_ascending) or is_good_level(front_bad_number, back_good_number, is_ascending)

        # We can only try removing middle number for the two sequential bad levels
        if len(bad_level_indices) == 2:
            bad_middle_index = bad_level_indices[1] # Second bad index is the middle index
            front_number, middle_number, back_number = report_numbers[bad_middle_index-1:bad_middle_index+2]
            part2_answer += is_good_level(front_number, back_number, is_ascending)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
