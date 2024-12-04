import re

crossword = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        crossword.append(line.strip())

sols = 0

# horizontal forward
for line in crossword:
    sols += len(re.findall(r'(XMAS)', line))

# horizontal backward
for line in crossword:
    sols += len(re.findall(r'(SAMX)', line))

crossword_rot = []
for x in range(len(crossword[0])):
    crossword_rot.append('')

for i, line in enumerate(crossword):
    for j, char in enumerate(line):
        crossword_rot[j] = crossword_rot[j]+char

# vertical forward
for line in crossword_rot:
    sols += len(re.findall(r'(XMAS)', line))

# vertical backward
for line in crossword_rot:
    sols += len(re.findall(r'(SAMX)', line))

crossword_rightshift = []
for i, line in enumerate(crossword):
    crossword_rightshift.append(i * " " + line + ((len(crossword[0]) - 1 - i) * " "))

crossword_rightshift_rot = []
for x in range(len(crossword_rightshift[0])):
    crossword_rightshift_rot.append('')

for i, line in enumerate(crossword_rightshift):
    for j, char in enumerate(line):
        crossword_rightshift_rot[j] = crossword_rightshift_rot[j]+char

# diagonal rightshift forward
for line in crossword_rightshift_rot:
    sols += len(re.findall(r'(XMAS)', line))

# diagonal rightshift backward
for line in crossword_rightshift_rot:
    sols += len(re.findall(r'(SAMX)', line))

crossword_leftshift = []
for i, line in enumerate(crossword):
    crossword_leftshift.append(((len(crossword[0]) - 1 - i) * " ") + line + i * " ")

crossword_leftshift_rot = []
for x in range(len(crossword_leftshift[0])):
    crossword_leftshift_rot.append('')

for i, line in enumerate(crossword_leftshift):
    for j, char in enumerate(line):
        crossword_leftshift_rot[j] = crossword_leftshift_rot[j]+char

# diagonal leftshift forward
for line in crossword_leftshift_rot:
    sols += len(re.findall(r'(XMAS)', line))

# diagonal leftshift backward
for line in crossword_leftshift_rot:
    sols += len(re.findall(r'(SAMX)', line))

print(sols)