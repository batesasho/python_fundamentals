import re

text = input()
pattern = r'(?<=(=|/))[A-Z][A-Za-z]{2,}(?=\1)'
new = [x.group() for x in re.finditer(pattern,text)]
print(f"Destinations: {', '.join(new)}")
print(f"Travel Points: {sum([len(new[x]) for x in range(len(new))])}")
