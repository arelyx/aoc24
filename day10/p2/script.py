num_map = dict()
pos_val_map = dict()
board = []
with open("input.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        line = line.strip()
        board.append(line)
        for j, char in enumerate(line):
            if not char in num_map:
                num_map[char] = set()
            num_map[char].add((i,j))
            pos_val_map[(i,j)] = int(char)
max_width = j
max_height = i

def is_neighbor(block, neighbor):
    return (abs(block[0] - neighbor[0]) == 1 and block[1] - neighbor[1] == 0) or \
    (abs(block[1] - neighbor[1]) == 1 and block[0] - neighbor[0] == 0)

out = 0
for trailhead in num_map['0']:
    paths = [[trailhead]]
    curr_blocks = {trailhead}
    for curr_level in range(1,10):
        next_blocks = set()
        for block in set(curr_blocks):
            neighbors = set()
            if block[0]-1 >= 0:
                neighbors.add((block[0]-1,block[1]))
            if block[1]-1 >= 0:
                neighbors.add((block[0],block[1]-1))
            if block[0]+1 <= max_height:
                neighbors.add((block[0]+1,block[1]))
            if block[1]+1 <= max_width:
                neighbors.add((block[0],block[1]+1))
            for neighbor in neighbors:
                if pos_val_map[neighbor] == curr_level:
                    next_blocks.add(neighbor)
        curr_blocks = next_blocks
        new_paths = []
        for path in paths:
            for block in next_blocks:
                if is_neighbor(block,path[-1]):
                    new_paths.append(path)
                    new_paths[-1] = new_paths[-1] + [block]
        paths = new_paths
        # print(f"level: {curr_level}")
        # for path in paths:
        #     print(f"> path: {path}")
    out += len(paths)
print(out)