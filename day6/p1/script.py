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
            guard_pos = coords

# where am i moving
# is something in front of me?
# not? move
# is? rotate
print(guard_pos)
visited = set()
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
    print(guard_pos)
    
    if not ((0 <= guard_pos[0] < max_pos[0]) and (0 <= guard_pos[1] < max_pos[1] )):
        print(len(visited))
        break