def character_calculation(char_one,char_two):
    returned_char_calc = ""
    for digit in range(ord(char_one)+1,ord(char_two)):
        returned_char_calc += chr(digit)
    return returned_char_calc

character_one = input()
character_two = input()

print(*character_calculation(character_one,character_two),sep=" ")