# I'm sorry python god... I didn't mean to write sh*t code...

part1_answer = 0
part2_answer = 0

grid = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        grid.append(input_line.strip())
width, height = len(grid[0]), len(grid)

tracked_plant_coords = set()
def find_region(row_index: int, col_index: int, parent_plant: str = None):
    if (row_index, col_index) in tracked_plant_coords:
        return []

    plant = grid[row_index][col_index]
    if parent_plant is not None and parent_plant != plant:
        return []

    tracked_plant_coords.add((row_index, col_index))

    region_coords = set([(row_index, col_index)])
    if row_index != 0:
        region_coords.update(find_region(row_index=row_index-1, col_index=col_index, parent_plant=plant))
    if row_index != height - 1:
        region_coords.update(find_region(row_index=row_index+1, col_index=col_index, parent_plant=plant))
    if col_index != 0:
        region_coords.update(find_region(row_index=row_index, col_index=col_index-1, parent_plant=plant))
    if col_index != width - 1:
        region_coords.update(find_region(row_index=row_index, col_index=col_index+1, parent_plant=plant))
    return region_coords

regions = []
for row_index in range(height):
    for col_index in range(width):
        plant = grid[row_index][col_index]
        if (row_index, col_index) not in tracked_plant_coords:
            regions.append(find_region(row_index=row_index, col_index=col_index))

has_top_fence = set()
has_bottom_fence = set()
has_left_fence = set()
has_right_fence = set()
for region in regions:
    parameter = 0
    for row_index, col_index in region:
        plant = grid[row_index][col_index]
        if row_index == 0 or grid[row_index-1][col_index] != plant:
            parameter += 1
            has_top_fence.add((plant, row_index, col_index))
        if row_index == height - 1 or grid[row_index+1][col_index] != plant:
            parameter += 1
            has_bottom_fence.add((plant, row_index, col_index))
        if col_index == 0 or grid[row_index][col_index-1] != plant:
            parameter += 1
            has_left_fence.add((plant, row_index, col_index))
        if col_index == width - 1 or grid[row_index][col_index+1] != plant:
            parameter += 1
            has_right_fence.add((plant, row_index, col_index))
    part1_answer += parameter * len(region)

accounted_sides = set()
for region in regions:
    num_sides = 0
    for row_index, col_index in region:
        plant = grid[row_index][col_index]
        if (plant, row_index, col_index) in has_top_fence and (row_index, col_index, "TOP_FENCE") not in accounted_sides:
            num_sides += 1
            accounted_sides.add((row_index, col_index, "TOP_FENCE"))
            movement = 1
            continue_right, continue_left = True, True
            while col_index - movement >= 0 or col_index + movement < width:
                if continue_right and (plant, row_index, col_index+movement) in has_top_fence:
                    accounted_sides.add((row_index, col_index+movement, "TOP_FENCE"))
                else:
                    continue_right = False
                if continue_left and (plant, row_index, col_index-movement) in has_top_fence:
                    accounted_sides.add((row_index, col_index-movement, "TOP_FENCE"))
                else:
                    continue_left = False
                if not (continue_right or continue_left):
                    break
                movement += 1
    
        if (plant, row_index, col_index) in has_bottom_fence and (row_index, col_index, "BOTTOM_FENCE") not in accounted_sides:
            num_sides += 1
            accounted_sides.add((row_index, col_index, "BOTTOM_FENCE"))
            movement = 1
            continue_right, continue_left = True, True
            while col_index - movement >= 0 or col_index + movement < width:
                if continue_right and (plant, row_index, col_index+movement) in has_bottom_fence:
                    accounted_sides.add((row_index, col_index+movement, "BOTTOM_FENCE"))
                else:
                    continue_right = False
                if continue_left and (plant, row_index, col_index-movement) in has_bottom_fence:
                    accounted_sides.add((row_index, col_index-movement, "BOTTOM_FENCE"))
                else:
                    continue_left = False
                if not (continue_right or continue_left):
                    break
                movement += 1
        
        if (plant, row_index, col_index) in has_left_fence and (row_index, col_index, "LEFT_FENCE") not in accounted_sides:
            num_sides += 1
            accounted_sides.add((row_index, col_index, "LEFT_FENCE"))
            movement = 1
            continue_down, continue_up = True, True
            while row_index - movement >= 0 or row_index + movement < height:
                if continue_down and (plant, row_index+movement, col_index) in has_left_fence:
                    accounted_sides.add((row_index+movement, col_index, "LEFT_FENCE"))
                else:
                    continue_down = False
                if continue_up and (plant, row_index-movement, col_index) in has_left_fence:
                    accounted_sides.add((row_index-movement, col_index, "LEFT_FENCE"))
                else:
                    continue_up = False
                if not (continue_down or continue_up):
                    break
                movement += 1
        
        if (plant, row_index, col_index) in has_right_fence and (row_index, col_index, "RIGHT_FENCE") not in accounted_sides:
            num_sides += 1
            accounted_sides.add((row_index, col_index, "RIGHT_FENCE"))
            movement = 1
            continue_down, continue_up = True, True
            while row_index - movement >= 0 or row_index + movement < height:
                if continue_down and (plant, row_index+movement, col_index) in has_right_fence:
                    accounted_sides.add((row_index+movement, col_index, "RIGHT_FENCE"))
                else:
                    continue_down = False
                if continue_up and (plant, row_index-movement, col_index) in has_right_fence:
                    accounted_sides.add((row_index-movement, col_index, "RIGHT_FENCE"))
                else:
                    continue_up = False
                if not (continue_down or continue_up):
                    break
                movement += 1
    part2_answer += num_sides * len(region)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
