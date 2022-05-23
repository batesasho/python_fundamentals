user_names = input().split(", ")
new = []
is_false = False
for el in user_names:
    if len(el) in range(3,17):
        for letter in el:
            if not (letter.isalpha() or letter == "-" or letter == "_" or letter.isdigit()):
                is_false = True
                break
        if is_false:
            is_false = False
            continue
        new.append(el)
else:
    print(*new,sep='\n')