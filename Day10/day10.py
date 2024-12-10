part1_answer = 0
part2_answer = 0

grid = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        grid.append(list(map(int, list(input_line.strip()))))
width, height = len(grid[0]), len(grid)

reachable_nines_tracker = {} # Tracks unique nines, useful for part 1
num_reachable_nines_tracker = {} # Tracks number of nines, useful for part 2
def run_dfs(row_idx: int, col_idx: int):
    coordinates = (row_idx, col_idx)
    if coordinates in reachable_nines_tracker:
        return reachable_nines_tracker[coordinates], num_reachable_nines_tracker[coordinates]

    trail_height = grid[row_idx][col_idx]

    reachable_nines = set()
    num_reachable_nines = 0
    if trail_height == 9:
        reachable_nines.add(coordinates)
        num_reachable_nines += 1
        return reachable_nines, num_reachable_nines

    if row_idx != 0 and grid[row_idx-1][col_idx] == trail_height + 1:
        nine_locations, num_nines = run_dfs(row_idx-1, col_idx)
        reachable_nines.update(nine_locations)
        num_reachable_nines += num_nines
    if row_idx != height-1 and grid[row_idx+1][col_idx] == trail_height + 1:
        nine_locations, num_nines = run_dfs(row_idx+1, col_idx)
        reachable_nines.update(nine_locations)
        num_reachable_nines += num_nines
    if col_idx != 0 and grid[row_idx][col_idx-1] == trail_height + 1:
        nine_locations, num_nines = run_dfs(row_idx, col_idx-1)
        reachable_nines.update(nine_locations)
        num_reachable_nines += num_nines
    if col_idx != width-1 and grid[row_idx][col_idx+1] == trail_height + 1:
        nine_locations, num_nines = run_dfs(row_idx, col_idx+1)
        reachable_nines.update(nine_locations)
        num_reachable_nines += num_nines
    
    reachable_nines_tracker[coordinates] = reachable_nines
    num_reachable_nines_tracker[coordinates] = num_reachable_nines
    return reachable_nines, num_reachable_nines

for row_idx in range(height):
    for col_idx in range(width):
        if grid[row_idx][col_idx] == 0:
            reachable_nines, sum_ratings = run_dfs(row_idx, col_idx)
            part1_answer += len(reachable_nines)
            part2_answer += sum_ratings

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
