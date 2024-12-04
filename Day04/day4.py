part1_answer = 0
part2_answer = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1),
}

grid = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        grid.append(list(input_line.strip()))
width, height = len(grid[0]), len(grid)

row_index, column_index = 0, 0
while row_index < height:
    while column_index < width:
        if grid[row_index][column_index] == "X":
            for vertical, horizontal in directions.values():
                if (row_index + (3*vertical) < 0 or
                    row_index + (3*vertical) >= height):
                    continue
                if (column_index + (3*horizontal) < 0 or
                    column_index + (3*horizontal) >= width):
                    continue
                if (grid[row_index + vertical][column_index + horizontal] == "M" and
                    grid[row_index + (2*vertical)][column_index + (2*horizontal)] == "A" and
                    grid[row_index + (3*vertical)][column_index + (3*horizontal)] == "S"):
                    part1_answer += 1

        if (grid[row_index][column_index] == "A" and
            row_index != 0 and row_index != height - 1 and
            column_index != 0 and column_index != width - 1):
            top_left = grid[row_index-1][column_index-1]
            top_right = grid[row_index-1][column_index+1]
            bottom_left = grid[row_index+1][column_index-1]
            bottom_right = grid[row_index+1][column_index+1]
            if (set([top_left, bottom_right]) == set(["M", "S"]) and
                set([top_right, bottom_left]) == set(["M", "S"])):
                part2_answer += 1

        column_index += 1
    column_index -= width
    row_index += 1

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
