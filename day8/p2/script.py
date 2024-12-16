board = []
height_limit = -1
with open("input.txt", "r") as f:
    for line in f.readlines():
        board.append(line.strip())
        height_limit += 1
width_limit = len(line.strip()) - 1

def get_pairs(locs):
    pairs = set()
    locs_ordered = list(locs)
    for loc_idx in range(len(locs_ordered)):
        for loc_offset_idx in range(len(locs_ordered[loc_idx:])):
            left_pair = locs_ordered[loc_idx]
            right_pair = locs_ordered[loc_idx+loc_offset_idx]
            if left_pair != right_pair:
                pairs.add((left_pair, right_pair))
    return pairs

antenna_loc = dict()

for i, line in enumerate(board):
    for j, char in enumerate(line):
        if char.isalpha() or char.isnumeric():
            if char not in antenna_loc:
                antenna_loc[char] = set()
            antenna_loc[char].add((i,j))
                

out = set()
for char in antenna_loc:
    if len(antenna_loc[char]) > 1:
        all_pairs = get_pairs(antenna_loc[char])
        for pair in all_pairs:
            pair_diff = (pair[0][0] - pair[1][0], pair[0][1] - pair[1][1])
            i = 0
            # print(f"{pair}: ", end="")
            while True:
                i += 1
                anti_1 = (pair[0][0] + (pair_diff[0] * i), pair[0][1] + (pair_diff[1] * i))
                anti_2 = (pair[1][0] - (pair_diff[0] * i), pair[1][1] - (pair_diff[1] * i))
                if 0 <= anti_1[0] <= width_limit and  0 <= anti_1[1] <= height_limit:
                    # print(anti_1, end="")
                    out.add(anti_1)
                if 0 <= anti_2[0] <= width_limit and  0 <= anti_2[1] <= height_limit:
                    # print(anti_2, end="")
                    out.add(anti_2)
                if not (0 <= anti_1[0] <= width_limit and  0 <= anti_1[1] <= height_limit or 0 <= anti_2[0] <= width_limit and  0 <= anti_2[1] <= height_limit):
                    break
            # print()

# i understand it now...
for char in antenna_loc:
    for pair in antenna_loc[char]:
        out.add(pair)
print(len(out))