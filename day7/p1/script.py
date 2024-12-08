sums = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sum, nums = line.strip().split(":")
        sums.append([sum,nums.strip().split(" ")])

total = 0
for sum in sums:
    curr_total = int(sum[0])
    possible_sums = set()
    for num in sum[1]:
        if len(possible_sums) == 0:
            possible_sums.add(int(num))
        else:
            new_possible_sums = set()
            for curr_sum in list(possible_sums):
                new_possible_sums.add(curr_sum * int(num))
                new_possible_sums.add(curr_sum + int(num))
            possible_sums = new_possible_sums
    if curr_total in possible_sums:
        total += curr_total
print(total)
