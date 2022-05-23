import re
number = int(input())


pattern = r"^(@#+)[A-Z][A-Za-z0-9]{4,}[A-Z](@#+)$"

for i in range(number):
    barcode_number = ''
    text = input()
    re_string = re.fullmatch(pattern,text)
    if re_string:
        barcode_number = "".join([x for x in re_string.group() if x.isdigit()])
        if barcode_number:
           print(f'Product group: {barcode_number}')
        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')

