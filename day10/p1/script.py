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

out = 0
for trailhead in num_map['0']:
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
    out += len(curr_blocks)
print(out)