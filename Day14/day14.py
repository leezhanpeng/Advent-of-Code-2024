import re
from copy import deepcopy
from typing import List, Dict

part1_answer = 0
part2_answer = 0

WIDTH, HEIGHT = 101, 103
TIMESTAMP_THRESHOLD = 10000

def calculate_safety_factor(robots: List[Dict]):
    top_left_count, top_right_count, bottom_left_count, bottom_right_count = 0, 0, 0, 0
    for robot in robots:
        px, py = robot["px"], robot["py"]
        top_left_count += px < WIDTH // 2 and py < HEIGHT // 2
        top_right_count += px > WIDTH // 2 and py < HEIGHT // 2
        bottom_left_count += px < WIDTH // 2 and py > HEIGHT // 2
        bottom_right_count += px > WIDTH // 2 and py > HEIGHT // 2
    return top_left_count * top_right_count * bottom_left_count * bottom_right_count

robots = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        px, py = map(int, re.search(r"p=(\d+),(\d+)", input_line).groups())
        vx, vy = map(int, re.search(r"v=(-?\d+),(-?\d+)", input_line).groups())
        robots.append({"px": px, "py": py, "vx": vx, "vy": vy})

lowest_safety_factor = float("inf")
lowest_safety_factor_time = None
lowest_safety_factor_robots = None

time = 0
while time < TIMESTAMP_THRESHOLD:
    for robot in robots:
        px, py, vx, vy = robot["px"], robot["py"], robot["vx"], robot["vy"]
        if time != 0:
            px = (px + vx) % WIDTH
            py = (py + vy) % HEIGHT
        robot["px"], robot["py"] = px, py
    safety_factor = calculate_safety_factor(robots)
    if time == 100:
        part1_answer = safety_factor
    if safety_factor < lowest_safety_factor:
        lowest_safety_factor = safety_factor
        lowest_safety_factor_time = time
        lowest_safety_factor_robots = deepcopy(robots)
    time += 1

# Making a bold assumption that the tree will appear before TIMESTAMP_THRESHOLD and
# that the tree exist on the timestamp with the lowest safety factor since the robots
# are likely clumped together in a quadrant
part2_answer = lowest_safety_factor_time

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")

# VISUALISATION FOR PART 2
input("Press enter to see the tree!")
grid = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
for robot in lowest_safety_factor_robots:
    px, py, vx, vy = robot["px"], robot["py"], robot["vx"], robot["vy"]
    grid[py][px] += 1
    robot["px"], robot["py"] = px, py
for row in grid:
    print("".join(map(lambda robot_count: " " if robot_count == 0 else "*", row)))
