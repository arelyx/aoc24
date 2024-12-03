import re
with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        valid_expr = re.findall(r'mul\(([0-9]*?),([0-9]*?)\)', line)
        for expr in valid_expr:
            # print(f"curr_expr: {expr} | running total: {total}")
            total += int(expr[0]) * int(expr[1])
print(total)