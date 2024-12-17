disk_zip = None
with open("input.txt", "r") as f:
    disk_zip = f.readline().strip()

def disk_builder(ordering, disk_struct):
    disk = ""
    for file in ordering:
        disk += disk_struct[file]["size"] * str(disk_struct[file]["id"])
        disk += disk_struct[file]["free"] * "."
    return disk

# create dictionary structure for disk_zip
disk_struct = {}
idx = 0
is_file = True
file_ordering = []
for size in disk_zip:
    if is_file:
        disk_struct[idx] = {"id":idx, "size":int(size), "free":0}
        file_ordering.append(idx)
    else:
        disk_struct[idx]["free"] = int(size)
        idx+=1
    is_file = not is_file

# must be n^2?
# print(disk_builder(file_ordering,disk_struct))

curr_task = idx
while curr_task >= 0:
    required_space = disk_struct[curr_task]["size"]
    # print(f"attempting task {curr_task}")
    for curr_canidate in file_ordering:
        # print(f"> checking if {curr_canidate} has space")
        if curr_canidate == curr_task:
            break
        if disk_struct[curr_canidate]["free"] >= required_space:
            # print(f"Can swap {curr_task} into {curr_canidate}'s free space!")
            left_task = file_ordering[file_ordering.index(curr_task) - 1]
            # next_task = curr_task - 1 # scary, off by one potential
            disk_struct[left_task]["free"] += disk_struct[curr_task]["size"] + disk_struct[curr_task]["free"]
            new_space = disk_struct[curr_canidate]["free"]
            remaining_space = new_space - required_space
            disk_struct[curr_task]["free"] = remaining_space
            disk_struct[curr_canidate]["free"] = 0

            del file_ordering[file_ordering.index(curr_task)]
            canidate_idx = file_ordering.index(curr_canidate)
            file_ordering.insert(canidate_idx+1, curr_task)
            # print(file_ordering)
            # print(disk_builder(file_ordering, disk_struct))
            break
    curr_task -= 1
cksum = 0
disk = disk_builder(file_ordering, disk_struct)
for idx, f_id in enumerate(disk):
    if f_id.isnumeric():
        cksum += idx * int(f_id)
    else:
        pass
print(cksum)