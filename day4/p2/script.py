crossword = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        crossword.append(line.strip())

crossword_pad = []
top_bottom = len(crossword[0]) * "." + ".."
crossword_pad.append(top_bottom)
for line in crossword:
    crossword_pad.append("." + line + ".")
crossword_pad.append(top_bottom)

ct = 0
for i,line in zip(range(1,len(crossword_pad)-1), crossword_pad[1:-1]):
    for j, char in zip(range(1,len(line)-1), line[1:-1]):
        if char == 'A':
            if (crossword_pad[i-1][j-1] == 'M' and crossword_pad[i+1][j+1] == 'S') or (crossword_pad[i-1][j-1] == 'S' and crossword_pad[i+1][j+1] == 'M'):
                if (crossword_pad[i-1][j+1] == 'M' and crossword_pad[i+1][j-1] == 'S') or (crossword_pad[i-1][j+1] == 'S' and crossword_pad[i+1][j-1] == 'M'):
                    ct += 1
print(ct)