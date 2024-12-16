sums = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        sum, nums = line.strip().split(":")
        sums.append([sum,nums.strip().split(" ")])

# hitting the reset because it's been a week...

# todo
# helper function to get all permutations of a number set
# helper function to get all possible sums (* or +) of a number set


def get_all_perms(nums):
    all_perms = []
    for i in range(len(nums)):
        if nums[0:i] != []:
            all_perms.append([nums[0:i],nums[i:len(nums)]])
    return all_perms

def get_all_sums(nums):
    possible_sums = set()
    for num in nums:
        if len(possible_sums) == 0:
            possible_sums.add(int(num))
        else:
            new_possible_sums = set()
            for curr_sum in list(possible_sums):
                new_possible_sums.add(curr_sum * int(num))
                new_possible_sums.add(curr_sum + int(num))
            possible_sums = new_possible_sums
    return possible_sums

total = 0
for sum in sums:
    # print(sum)
    curr_target = sum[0]
    curr_numbers = sum[1]
    if int(curr_target) in get_all_sums(curr_numbers):
        total = total+int(curr_target)
    else:
        curr_perms = get_all_perms(curr_numbers)
        for curr_perm in curr_perms:
            left_all_sums = get_all_sums(curr_perm[0])
            right_all_sums = get_all_sums(curr_perm[1])
            for l_val in list(left_all_sums):
                for r_val in list(right_all_sums):
                    if str(l_val) + str(r_val) == str(curr_target):
                        total = total+int(curr_target)

print(total)

# MISUNDERSTOOD!!