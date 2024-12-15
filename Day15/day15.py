part1_answer = 0
part2_answer = 0

direction = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}
expansion = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}

part1_grid = []
part2_grid = []
moves = ""
part1_robot_index = None
part2_robot_index = None
with open("input.txt", "r") as input_file:
    drawing_grid = True
    for input_line in input_file:
        trimmed_input_line = input_line.strip()
        if trimmed_input_line == "":
            drawing_grid = False
        elif drawing_grid:
            if "@" in trimmed_input_line:
                part1_robot_index = (len(part1_grid), trimmed_input_line.index("@"))
            part1_grid.append(list(trimmed_input_line))

            expanded_grid_row = "".join(map(lambda tile: expansion[tile], trimmed_input_line))
            if "@" in expanded_grid_row:
                part2_robot_index = (len(part2_grid), expanded_grid_row.index("@"))
            part2_grid.append(list(expanded_grid_row))
        else:
            moves += trimmed_input_line
part1_width, part1_height = len(part1_grid[0]), len(part1_grid)
part2_width, part2_height = len(part2_grid[0]), len(part2_grid)

def part1_push(row_index: int, col_index: int, tile_direction: str):
    if part1_grid[row_index][col_index] == ".":
        return True

    if part1_grid[row_index][col_index] == "#":
        return False

    movement = direction[tile_direction]
    if part1_push(row_index + movement[0], col_index + movement[1], tile_direction):
        part1_grid[row_index+movement[0]][col_index+movement[1]] = part1_grid[row_index][col_index]
        part1_grid[row_index][col_index] = "."
        return True

    return False

# Applicable only for up/down movements
def part2_check_pushable(row_index: int, col_index: int, tile_direction: str):
    if part2_grid[row_index][col_index] == ".":
        return True
    
    if part2_grid[row_index][col_index] == "#":
        return False

    movement = direction[tile_direction]
    pushable = part2_check_pushable(row_index+movement[0], col_index, tile_direction)
    if part2_grid[row_index][col_index] == "@":
        return pushable

    if not pushable:
        return False

    if part2_grid[row_index][col_index] == "[":
        return part2_check_pushable(row_index+movement[0], col_index+1, tile_direction)
    elif part2_grid[row_index][col_index] == "]":
        return part2_check_pushable(row_index+movement[0], col_index-1, tile_direction)

def part2_push(row_index: int, col_index: int, tile_direction: str):
    if part2_grid[row_index][col_index] == ".":
        return True
    
    if part2_grid[row_index][col_index] == "#":
        return False

    movement = direction[tile_direction]
    if tile_direction in ["<", ">"]:
        if part2_push(row_index + movement[0], col_index + movement[1], tile_direction):
            part2_grid[row_index+movement[0]][col_index+movement[1]] = part2_grid[row_index][col_index]
            part2_grid[row_index][col_index] = "."
            return True
        else:
            return False
    
    if part2_grid[row_index][col_index] == "@" and not part2_check_pushable(row_index, col_index, tile_direction):
        return False

    if tile_direction in ["^", "v"]:
        if part2_grid[row_index][col_index] == "]":
            col_index -= 1

        part2_push(row_index + movement[0], col_index, tile_direction)
        if part2_grid[row_index][col_index] != "@" and part2_grid[row_index+movement[0]][col_index] != "[":
            part2_push(row_index + movement[0], col_index+1, tile_direction)

        if part2_grid[row_index][col_index] != "@":
            part2_grid[row_index+movement[0]][col_index+1] = part2_grid[row_index][col_index+1]
            part2_grid[row_index][col_index+1] = "."
        part2_grid[row_index+movement[0]][col_index] = part2_grid[row_index][col_index]
        part2_grid[row_index][col_index] = "."

        return True

    return False

for move in moves:
    robot_has_moved_part1 = part1_push(part1_robot_index[0], part1_robot_index[1], move)
    if robot_has_moved_part1:
        part1_robot_index = (part1_robot_index[0]+direction[move][0], part1_robot_index[1]+direction[move][1])

    robot_has_moved_part2 = part2_push(part2_robot_index[0], part2_robot_index[1], move)
    if robot_has_moved_part2:
        part2_robot_index = (part2_robot_index[0]+direction[move][0], part2_robot_index[1]+direction[move][1])

for row_index in range(part1_height):
    for col_index in range(part1_width):
        if part1_grid[row_index][col_index] == "O":
            part1_answer += row_index * 100 + col_index

for row_index in range(part2_height):
    for col_index in range(part2_width):
        if part2_grid[row_index][col_index] == "[":
            part2_answer += row_index * 100 + col_index

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
