import re
command = input()
pattern = r'\d+'
new = []
while bool(command):
    seq = re.finditer(pattern,command)
    new.extend(seq)
    command = input()
else:
    print(*[x.group() for x in new],sep=" ")