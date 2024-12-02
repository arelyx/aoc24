ll = list()
rl = list()

with open("input.txt", "r") as f:
    for x in f.readlines():
        l = int(x.split(" ")[0])
        r = int(x.split(" ")[3].strip("\n"))
        ll.append(l)
        rl.append(r)

ll = sorted(ll)
rl = sorted(rl)

dist = 0
for l,r in zip(ll, rl):
    dist += abs(r - l)

print(dist)