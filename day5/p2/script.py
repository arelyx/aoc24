# given pairs of what can and cannot be before/after a particular page number.
import json
ordering = []
with open("input.txt", "r") as f:
    breakpoint = False
    prev_disallow = {}
    next_disallow = {}
    for line in f.readlines():
        curr = line.strip()
        if curr == "":
            breakpoint = True
        elif breakpoint == False:
            pair = curr.split("|")
            if pair[0] not in prev_disallow:
                prev_disallow[pair[0]] = [pair[1]]
            else:
                prev_disallow[pair[0]].append(pair[1])
            if pair[1] not in next_disallow:
                next_disallow[pair[1]] = [pair[0]]
            else:
                next_disallow[pair[1]].append(pair[0])
        elif breakpoint == True:
            ordering.append(curr.split(","))

mid_page_sum = 0

for i, pages in enumerate(ordering):
    # print(pages)
    valid = True
    for j, page in enumerate(pages):
        prev = pages[:j]
        next = pages[j+1:]
        for prev_page in prev:
            if prev_page in prev_disallow[page]:
                valid = False
        for next_page in next:
            if next_page in next_disallow[page]:
                valid = False
    if not valid:
        corrected_pages = []
        for j, page in enumerate(pages):
            corrected_pages.insert(0, page)
            for curr_pos in range(len(corrected_pages)):
                for k, c_page in zip(range(curr_pos,len(corrected_pages)), corrected_pages[curr_pos:]):
                    if c_page in next_disallow[corrected_pages[curr_pos]]:
                        corrected_pages.pop(curr_pos)
                        corrected_pages.insert(curr_pos + 1, page)
                        break
            
                
        mid_page = corrected_pages[int((len(corrected_pages) + 1) / 2) -1] # all valid happen to be odd?
        mid_page_sum += int(mid_page)
print(mid_page_sum)