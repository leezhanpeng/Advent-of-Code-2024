import heapq

part1_answer = 0
part2_answer = 0

# Clockwise
directions = {
    0: (-1, 0),
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
}

STARTING_DIRECTION_INDEX = 1

grid = []
starting_pos = None
ending_pos = None
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        trimmed_input_line = input_line.strip()
        if "S" in trimmed_input_line:
            starting_pos = (len(grid), trimmed_input_line.index("S"))
        if "E" in trimmed_input_line:
            ending_pos = (len(grid), trimmed_input_line.index("E"))
        grid.append(trimmed_input_line)

lowest_score = float("inf")
heap = []
heapq.heappush(heap, (0, starting_pos, STARTING_DIRECTION_INDEX, []))
cost_track = {}
best_path_tiles = set([starting_pos, ending_pos])
while heap:
    score, location, direction_index, path_history = heapq.heappop(heap)
    if score > lowest_score:
        break

    if grid[location[0]][location[1]] == "E":
        lowest_score = score
        best_path_tiles.update(path_history)
        continue
    
    cost = cost_track.get((location, direction_index), float("inf"))
    if cost < score:
        continue

    cost_track[(location, direction_index)] = score

    # Move
    movement = directions[direction_index]
    next_location = (location[0]+movement[0], location[1]+movement[1])
    if grid[next_location[0]][next_location[1]] != "#":
        path_history_copy = path_history.copy()
        path_history_copy.append(location)
        heapq.heappush(heap, (score+1, next_location, direction_index, path_history_copy))

    # Turn
    clockwise_index = (direction_index + 1) % 4
    heapq.heappush(heap, (score+1000, location, clockwise_index, path_history.copy()))
    counterclockwise_index = (direction_index - 1) % 4
    heapq.heappush(heap, (score+1000, location, counterclockwise_index, path_history.copy()))

part1_answer = lowest_score
part2_answer = len(best_path_tiles)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
