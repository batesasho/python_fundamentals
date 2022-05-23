command = input()

digit = ''
letters =''
others = ''


for el in command:
    if el.isdigit():
        digit += el
    elif el.isalpha():
        letters += el

    else:
        others += el
print(digit)
print(letters)
print(others)
