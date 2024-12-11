part1_answer = 0
part2_answer = 0

memoised_splits = {}
def split_stones(number: str, blinks: int):
    if blinks == 0:
        return 1

    number = str(int(number)) # Remove leading 0s

    if (number, blinks) in memoised_splits:
        return memoised_splits[(number, blinks)]

    if number == "0":
        num_stones = split_stones("1", blinks-1)
    elif len(number) % 2 == 0:
        num_stones = split_stones(number[:len(number)//2], blinks-1) + split_stones(number[len(number)//2:], blinks-1)
    else:
        num_stones = split_stones(str(int(number)*2024), blinks-1)

    memoised_splits[(number, blinks)] = num_stones
    return num_stones

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        stones = input_line.strip().split(" ")
        for stone in stones:
            part1_answer += split_stones(stone, blinks=25)
            part2_answer += split_stones(stone, blinks=75)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
