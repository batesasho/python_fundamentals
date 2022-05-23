import re
text = input()
pattern = r'\+359(-| )2\1\d{3}\1\d{4}\b'

new = re.finditer(pattern,text)
new = [x.group() for x in new]
print(", ".join(new))
