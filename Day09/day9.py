part1_answer = 0
part2_answer = 0

whole_file_tracker = {}
space_tracker = []
location_pointer = 0
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        numbers_original = list(map(int, list(input_line.strip())))

    numbers = numbers_original.copy()
    current_position = 0
    front_pointer_index, back_pointer_index = 0, len(numbers) - 1
    insertion_queue = []
    queue_pointer = 0
    while front_pointer_index <= back_pointer_index:
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
            numbers[back_pointer_index] -= 1

        for _ in range(numbers[front_pointer_index]):
            part1_answer += current_position * insertion_queue[queue_pointer]
            queue_pointer += 1
            current_position += 1
            
            numbers[front_pointer_index] -= 1
            if queue_pointer == len(insertion_queue):
                break
        
        if numbers[front_pointer_index] == 0:
            front_pointer_index += 1

        if queue_pointer == len(insertion_queue):
            back_pointer_index -= 1

    # Leftovers in the queue, guaranteed no clash
    for index in range(queue_pointer, len(insertion_queue)):
        part1_answer += current_position * insertion_queue[index]
        current_position += 1

    for index in range(len(numbers_original)):
        amount = numbers_original[index]
        if index % 2 == 0:
            whole_file_tracker[index // 2] = [location_pointer, amount]
            location_pointer += amount
        else:
            space_tracker.append([location_pointer, amount])
            location_pointer += amount

    for id in range(len(numbers_original) // 2, -1, -1):
        location, size = whole_file_tracker[id]
        for space_tracker_index in range(len(space_tracker)):
            space_location, space_amount = space_tracker[space_tracker_index]
            if location > space_location and size <= space_amount:
                space_tracker[space_tracker_index][0] += size
                space_tracker[space_tracker_index][1] -= size
                whole_file_tracker[id][0] = space_location
                break
    
    for id, [location, amount] in whole_file_tracker.items():
        for each_amount in range(amount):
            part2_answer += id * (location + each_amount)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
