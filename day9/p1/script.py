disk_zip = None
with open("input.txt", "r") as f:
    disk_zip = f.readline().strip()

is_file = True
idx = 0
disk = ""
for size in disk_zip:
    if is_file:
        disk = disk + str(idx) * int(size)
        idx+=1
    else:
        disk = disk + "." * int(size)
    is_file = not is_file

disk = list(disk)
disk_len = len(disk)
# print(disk_len)
while True:
    next_free = None
    next_move = None
    for i, val in enumerate(disk):
        if val == ".":
            next_free = i
            break
    for i_offset, val in enumerate(reversed(disk)):
        i = disk_len - i_offset - 1 
        if val != ".":
            next_move = i
            break
    disk[next_free], disk[next_move] = disk[next_move], disk[next_free]
    if next_free == next_move - 1:
        break
    # print(len(str(next_move)))

cksum = 0
for idx, f_id in enumerate(disk):
    if f_id.isnumeric():
        cksum += idx * int(f_id)
    else:
        break
print(cksum)