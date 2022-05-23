import re
text = input()
pattern = r'>>(?P<Furniture>[A-Za-z]+)<<(?P<Price>\d+(\.\d+)?)!(?P<Quantity>\d+)'
total_money = 0
furn_name = []
while not text == "Purchase":
    processed = re.fullmatch(pattern,text)
    if processed:
        current_price = 0
        furniture = processed.groupdict()['Furniture']
        price = float(processed.groupdict()['Price'])
        quantity = int(processed.groupdict()['Quantity'])
        current_price = quantity * price
        total_money += current_price
        furn_name.append(furniture)
    text = input()
else:
    print("Bought furniture:")
    if furn_name:
        print('\n'.join(furn_name))
    print(f"Total money spend: {(total_money):.2f}")