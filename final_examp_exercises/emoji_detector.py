import re

text = input()
pattern = r'(::|\*\*)[A-Z][a-z]{2,}\1'
pattern_digits = r'\d'
numbers =[int(y) for y in re.findall(pattern_digits,text)]

cool_number = 1
for i in range(len(numbers)):
    cool_number *= numbers[i]

seq_dict = {}
seq = [x.group() for x in re.finditer(pattern,text)]

for el in range(len(seq)):
    ascii_value = 0
    ascii_value = sum([ord(x) for x in seq[el] if x.isalpha()])
    seq_dict.setdefault(seq[el],ascii_value)

print(f"Cool threshold: {cool_number}")
print(f"{len(seq_dict)} emojis found in the text. The cool ones are:")
seq_dict = {key:value for key,value in seq_dict.items() if value > cool_number}
[print(*seq_dict.keys(),sep ='\n')]