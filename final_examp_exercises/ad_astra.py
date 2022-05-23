import re

text = input()

pattern = r'(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<dates>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1'

data = [x.groupdict() for x in re.finditer(pattern,text)]

total_cal = sum([int(data[i]['calories']) for i in range(len(data))])

print(f"You have food to last you for: {int(total_cal/2000)} days!")

[print(f"Item: {data[el]['name']}, Best before: {data[el]['dates']}, Nutrition: {data[el]['calories']}") for el in range(len(data))]


