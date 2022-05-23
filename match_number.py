import re

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'


seq = re.finditer(pattern,input())

print(*[x.group() for x in seq])