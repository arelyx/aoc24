blinks = 75
with open("input.txt", "r") as f:
    stones = f.readline().strip().split(" ")
# print(stones)
for blink in range(blinks):
    new_stones = []
    for stone in stones:
        if stone == '0':
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            stone_length = len(stone)
            new_stones.append(stone[:int(stone_length/2)])
            new_stones.append(str(int(stone[int(stone_length/2):])))
        else:
            new_stones.append(str(int(stone)*2024))
    stones = new_stones
    # print(f"level {blink} has ct {len(stones)}")
print(stones)