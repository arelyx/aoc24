maze = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        maze.append([])
        for char in line.strip():
            maze[-1].append(char)

direction = "UP"
guard_pos = None
obs = set()
max_pos = (len(maze), len(maze[0]))
for i, line in enumerate(maze):
    for j, char in enumerate(line):
        coords = (i,j)
        if char == "#":
            obs.add(coords)
        elif char == ".":
            pass
        else:
            og_guard_pos = coords

loop_ct = 0
og_obs = set(obs)
obs = None
for i in range(max_pos[0]):
    for j in range(max_pos[1]):
        guard_pos = og_guard_pos
        direction = "UP"
        obs = set(og_obs)
        obs.add((i,j))
        visited = set()
        revisit_ct = 0
        while True:
            visited.add(guard_pos)
            if direction == "UP":
                next_pos = (guard_pos[0]-1, guard_pos[1])
                if next_pos in obs:
                    direction = "RIGHT"
                else:
                    guard_pos = next_pos
            elif direction == "RIGHT":
                next_pos = (guard_pos[0], guard_pos[1]+1)
                if next_pos in obs:
                    direction = "DOWN"
                else:
                    guard_pos = next_pos
            elif direction == "DOWN":
                next_pos = (guard_pos[0]+1, guard_pos[1])
                if next_pos in obs:
                    direction = "LEFT"
                else:
                    guard_pos = next_pos
            elif direction == "LEFT":
                next_pos = (guard_pos[0], guard_pos[1]-1)
                if next_pos in obs:
                    direction = "UP"
                else:
                    guard_pos = next_pos
            if guard_pos in visited:
                revisit_ct += 1
                if revisit_ct == 1000: ## brute force, idc...
                    loop_ct += 1
                    break
            # print(f"guard_pos: {guard_pos}, obs pos: {(i,j)}")
            if not ((0 <= guard_pos[0] < max_pos[0]) and (0 <= guard_pos[1] < max_pos[1] )):
                # print(f"guard_pos: {guard_pos}, obs pos: {(i,j)}")
                break
    print(f"Done with {i}/{max_pos[0]}")
print(loop_ct)