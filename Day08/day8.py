part1_answer = 0
part2_answer = 0

grid = []
antenna_coordinates = {}
with open("input.txt", "r") as input_file:
    row_index = 0
    for input_line in input_file:
        row = list(input_line.strip())
        grid.append(row)

        for column_index in range(len(row)):
            antenna = row[column_index]
            if antenna == ".":
                continue
            antenna_coordinates[antenna] = antenna_coordinates.get(antenna, [])
            antenna_coordinates[antenna].append((row_index, column_index))

        row_index += 1

width, height = len(grid[0]), len(grid)

existing_antinode_locations_part1 = set()
existing_antinode_locations_part2 = set()
for antenna, locations in antenna_coordinates.items():
    if len(locations) < 2:
        continue

    for first_antenna_idx in range(1, len(locations)):
        for second_antenna_idx in range(first_antenna_idx):
            first_antenna_location = locations[first_antenna_idx]
            second_antenna_location = locations[second_antenna_idx]
            row_antenna_distance = second_antenna_location[0] - first_antenna_location[0]
            col_antenna_distance = second_antenna_location[1] - first_antenna_location[1]

            first_antinode_location = (second_antenna_location[0] + row_antenna_distance, second_antenna_location[1] + col_antenna_distance)
            second_antinode_location = (first_antenna_location[0] - row_antenna_distance, first_antenna_location[1] - col_antenna_distance)

            if 0 <= first_antinode_location[0] < height and 0 <= first_antinode_location[1] < width:
                existing_antinode_locations_part1.add(first_antinode_location)
            if 0 <= second_antinode_location[0] < height and 0 <= second_antinode_location[1] < width:
                existing_antinode_locations_part1.add(second_antinode_location)

            existing_antinode_locations_part2.add(first_antenna_location)
            existing_antinode_locations_part2.add(second_antenna_location)
            while 0 <= first_antinode_location[0] < height and 0 <= first_antinode_location[1] < width:
                existing_antinode_locations_part2.add(first_antinode_location)
                first_antinode_location = (first_antinode_location[0] + row_antenna_distance, first_antinode_location[1] + col_antenna_distance)
            while 0 <= second_antinode_location[0] < height and 0 <= second_antinode_location[1] < width:
                existing_antinode_locations_part2.add(second_antinode_location)
                second_antinode_location = (second_antinode_location[0] - row_antenna_distance, second_antinode_location[1] - col_antenna_distance)

part1_answer = len(existing_antinode_locations_part1)
part2_answer = len(existing_antinode_locations_part2)

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
