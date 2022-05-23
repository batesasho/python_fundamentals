import re
text = input()
pattern= r'(?<=\s)[A-Za-z0-9]+[a-z0-9.\-_]*@[a-z]+[a-z\-]*(\.[a-z]+)+'

valid = [el.group() for el in re.finditer(pattern,text)]
print(*valid,sep="\n")