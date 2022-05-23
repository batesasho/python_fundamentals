command = input().split()
total_sum = 0
number_letter_alphabet = 0

for el in range(len(command)):
    first_letter = command[el][0]
    last_letter = command[el][-1]
    number = int(command[el][1:-1])
    sum = 0
    if first_letter.isupper():
        number_letter_alphabet = ord(first_letter) - 64
        sum = number/number_letter_alphabet
    elif first_letter.islower():
        number_letter_alphabet = ord(first_letter) - 96
        sum = number * number_letter_alphabet

    if last_letter.isupper():
        number_letter_alphabet = ord(last_letter) - 64
        sum -= number_letter_alphabet
    elif last_letter.islower():
        number_letter_alphabet = ord(last_letter) - 96
        sum += number_letter_alphabet

    total_sum += sum
else:
    print(f"{total_sum:.2f}")
        

