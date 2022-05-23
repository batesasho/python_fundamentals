import re
pattern = r'(^_|(?<=\s_))[A-Za-z]+\b'

print(*(re.finditer(pattern,input())))

