part1_answer = 0
part2_answer = 0

with open("input.txt", "r") as input_file:
    for input_line in input_file:
        numbers = list(map(int, list(input_line.strip())))

        current_position = 0
        front_pointer_index, back_pointer_index = 0, len(numbers) - 1
        insertion_queue = []
        queue_pointer = 0
        while front_pointer_index != back_pointer_index:
            if front_pointer_index % 2 == 0:
                amount = numbers[front_pointer_index]
                for _ in range(amount):
                    part1_answer += current_position * (front_pointer_index // 2)
                    current_position += 1
                front_pointer_index += 1
                continue

            if back_pointer_index % 2 != 0:
                back_pointer_index -= 1
                continue

            for _ in range(numbers[back_pointer_index]):
                insertion_queue.append(back_pointer_index // 2)

            for _ in range(numbers[front_pointer_index]):
                part1_answer += current_position * insertion_queue[queue_pointer]
                queue_pointer += 1
                current_position += 1
            front_pointer_index += 1
            back_pointer_index -= 1

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
