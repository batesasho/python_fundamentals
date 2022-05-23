import re

number = int(input())

pattern = r'(\*|\@)(?P<tag>[A-Z][a-z]{2,})\1\:\s{1}(\[(?P<letter_one>[A-Za-z])\]\|)(\[(?P<letter_two>[A-Za-z])\]\|)(\[(?P<letter_three>[A-Za-z])\]\|)$'
new = {}

for i in range(number):
    text = input()
    new = [x.groupdict() for x in re.finditer(pattern,text)]
    if new:
        new = [x.groupdict() for x in re.finditer(pattern,text)][0]
        print(f'{new["tag"]}: {ord((new["letter_one"]))} {ord((new["letter_two"]))} {ord((new["letter_three"]))}')
    else:
        print("Valid message not found!")






