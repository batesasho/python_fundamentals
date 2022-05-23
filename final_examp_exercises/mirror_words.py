import re

text = input()

pattern = r'(@|#)[A-Za-z]{3,}\1{2}[A-Za-z]{3,}\1'

list_words = [x.group() for x in re.finditer(pattern,text)]

new = []

if list_words:
    print(f"{len(list_words)} word pairs found!")
else:
    print("No word pairs found!")

for el in list_words:
    patt = r'[@#]'
    command = re.split(patt,el)
    if command[1] == command[3][::-1]:
        new.append([command[1],command[3]])
else:
    if new:
        print("The mirror words are:")
        print(*[f"{new[x][0]} <=> {new[x][1]}" for x in range(len(new))],sep = ", ")
    else:
        print("No mirror words!")



