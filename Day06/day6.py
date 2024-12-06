import time

start_time = time.perf_counter()

part1_answer = 0
part2_answer = 0

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
clockwise = ["^", ">", "v", "<"]

grid = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        grid.append(list(input_line.strip()))

start_position = None
for column_index, row in enumerate(grid):
    for direction in directions.keys():
        if direction in row:
            start_position = (column_index, row.index(direction))
            break
    if start_position:
        break

visited = set()
position = start_position
current_direction_index = clockwise.index(grid[position[0]][position[1]])
while True:
    if position not in visited:
        part1_answer += 1
    visited.add(position)

    escaped = False
    new_position = None
    while new_position is None:
        direction = directions[clockwise[current_direction_index]]
        potential_new_position = (position[0] + direction[0], position[1] + direction[1])

        if (potential_new_position[0] < 0 or
            potential_new_position[0] >= len(grid) or
            potential_new_position[1] < 0 or
            potential_new_position[1] >= len(grid[0])):
            escaped = True
            break

        if grid[potential_new_position[0]][potential_new_position[1]] == "#":
            current_direction_index += 1
            if current_direction_index == 4:
                current_direction_index = 0
        else:
            new_position = potential_new_position

    if escaped:
        break

    position = new_position


for row_index, col_index in visited:
    if start_position == (row_index, col_index):
        continue

    grid[row_index][col_index] = "#"

    visited_map = {}
    position = start_position
    current_direction_index = clockwise.index(grid[position[0]][position[1]])

    while True:
        visited_map[position] = visited_map.get(position, set())
        direction = directions[clockwise[current_direction_index]]
        if direction in visited_map[position]:
            part2_answer += 1
            break
        else:
            visited_map[position].add(direction)

        escaped = False
        new_position = None
        while new_position is None:
            direction = directions[clockwise[current_direction_index]]
            potential_new_position = (position[0] + direction[0], position[1] + direction[1])

            if (potential_new_position[0] < 0 or
                potential_new_position[0] >= len(grid) or
                potential_new_position[1] < 0 or
                potential_new_position[1] >= len(grid[0])):
                escaped = True
                break

            if grid[potential_new_position[0]][potential_new_position[1]] == "#":
                current_direction_index += 1
                if current_direction_index == 4:
                    current_direction_index = 0
            else:
                new_position = potential_new_position

        if escaped:
            break

        position = new_position

    grid[row_index][col_index] = "."

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")

end_time = time.perf_counter()
time_taken = end_time - start_time
print(f"Time taken: {time_taken} seconds") # 18 Seconds...
