command = input()
final_string  = ''
temp_str = ''

el = 0
while el < len(command):
    if not command[el].isdigit():
        temp_str += command[el].upper()

    else:
        digit = ''
        for i in range(el,len(command)):
            if command[i].isdigit():
                digit += command[i]
            else:
                break
        temp_str *= int(digit)
        final_string += temp_str
        temp_str = ''

    el+=1
else:
    print(f"Unique symbols used: {len(set(final_string))}")
    print(final_string)

