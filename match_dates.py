import re
text = input()
pattern = r'(?P<Day>\d{2})([./-])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})'
new = [x.groupdict() for x in re.finditer(pattern,text)]
[print(f"Day: {x['Day']}, Month: {x['Month']}, Year: {x['Year']}") for x in new]
