import re
with open("input.txt", "r") as f:
    total = 0
    do = True
    for line in f.readlines():
        valid_expr = re.findall(r'mul\(([0-9]*?),([0-9]*?)\)|(don\'t\(\))|(do\(\))', line)
        for expr in valid_expr:
            if expr[2] == "don't()":
                do = False
            elif expr[3] == "do()":
                do = True
            elif do == True:
                # print(f"curr_expr: {expr} | running total: {total}")
                total += int(expr[0]) * int(expr[1])
print(total)