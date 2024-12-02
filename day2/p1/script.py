safe_ct = 0
with open("input.txt", "r") as f:
    for l in f.readlines():
        curr = l.strip().split(" ")
        for i, val in enumerate(curr):
            curr[i] = int(val)
        safe = True
        prev = None
        incr = None
        for val in curr:
            if prev == None:
                prev = val
            elif incr == None:
                if val > prev:
                    incr = True
                else:
                    incr = False
                if abs(val - prev) > 3 or val - prev == 0:
                    safe = False
            elif abs(val - prev) > 3 or val - prev == 0:
                safe = False
            elif val > prev and incr == False:
                safe = False
            elif val < prev and incr == True:
                safe = False
            prev = val
        if safe == True:
            safe_ct += 1
        #     print(f"Safe:  ", end="")
        # else:
        #     print(f"!Safe: ", end="")
        # print(curr)

print(safe_ct)