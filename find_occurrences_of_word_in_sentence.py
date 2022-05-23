import re

text = input()
spec_word = input()

seq = re.findall(rf'\b{spec_word}\b',text,flags=re.IGNORECASE)

print(len(seq))