import heapq

part1_answer = 0
part2_answer = 0

MEMORY_SIZE = 71

memory = [["." for _ in range(MEMORY_SIZE)] for _ in range(MEMORY_SIZE)]
bytes = []
with open("input.txt", "r") as input_file:
    for input_line in input_file:
        bytes.append(tuple(map(int, input_line.strip().split(","))))

for index in range(1023):
    byte = bytes[index]
    memory[byte[0]][byte[1]] = "#"

# Checking for every dropped byte, but it's fine...
# Based on the question, we kind of guarantee that 1024 bytes on the map can still find a solution. So we just start from dropping 1024th byte to include part1 answer
for index in range(1023, len(bytes)):
    byte = bytes[index]
    memory[byte[0]][byte[1]] = "#"

    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    tracked_bytes = set()
    has_path = False
    while heap:
        steps, location = heapq.heappop(heap)
        if location == (MEMORY_SIZE - 1, MEMORY_SIZE - 1):
            if index == 1023:
                part1_answer = steps
            has_path = True
            break

        up, down, left, right = (location[0]-1, location[1]), (location[0]+1, location[1]), (location[0], location[1]-1), (location[0], location[1]+1)
        if up not in tracked_bytes and 0 <= up[0] < MEMORY_SIZE and 0 <= up[1] < MEMORY_SIZE and memory[up[0]][up[1]] == ".":
            tracked_bytes.add(up)
            heapq.heappush(heap, (steps+1, up))
        if down not in tracked_bytes and 0 <= down[0] < MEMORY_SIZE and 0 <= down[1] < MEMORY_SIZE and memory[down[0]][down[1]] == ".":
            tracked_bytes.add(down)
            heapq.heappush(heap, (steps+1, down))
        if left not in tracked_bytes and 0 <= left[0] < MEMORY_SIZE and 0 <= left[1] < MEMORY_SIZE and memory[left[0]][left[1]] == ".":
            tracked_bytes.add(left)
            heapq.heappush(heap, (steps+1, left))
        if right not in tracked_bytes and 0 <= right[0] < MEMORY_SIZE and 0 <= right[1] < MEMORY_SIZE and memory[right[0]][right[1]] == ".":
            tracked_bytes.add(right)
            heapq.heappush(heap, (steps+1, right))

    if not has_path:
        part2_answer = f"{byte[0]},{byte[1]}"
        break

print(f"Part 1 Answer: {part1_answer}")
print(f"Part 2 Answer: {part2_answer}")
