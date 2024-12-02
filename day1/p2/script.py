ll = list()
rd = dict()

with open("input.txt", "r") as f:
    for x in f.readlines():
        l = int(x.split(" ")[0])
        r = int(x.split(" ")[3].strip("\n"))
        ll.append(l)
        if r in rd:
            rd[r] += 1
        else:
            rd[r] = 1

dist = 0
for l in ll:
    if l in rd:
        dist += l * rd[l]

print(dist)