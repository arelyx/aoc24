disk_zip = None
with open("input.txt", "r") as f:
    disk_zip = f.readline().strip()

is_file = True
idx = 0
disk = []
for size in disk_zip:
    if is_file:
        disk = disk + [str(idx)] * int(size)
        idx+=1
    else:
        disk = disk + ["."] * int(size)
    is_file = not is_file

disk = list(disk)
disk_len = len(disk)
next_free = 0
next_move = disk_len -1
while True:
    while True:
        if disk[next_free] == ".":
            break
        next_free+=1

    while True:
        if disk[next_move] != ".":
            break
        next_move -= 1
    if next_free >= next_move:
        break
    disk[next_free], disk[next_move] = disk[next_move], disk[next_free]
cksum = 0
for idx, f_id in enumerate(disk):
    if f_id.isnumeric():
        cksum += idx * int(f_id)
    else:
        break
print(cksum)