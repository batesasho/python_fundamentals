import re
command =input().replace(" ","").split(",")
pattern = r"[@$&^]{6,11}"

for el in command:
    if len(el) == 20:
        left = el[:int(len(el) / 2)]
        right = el[int(len(el) / 2):]
        left_fil = "".join(re.findall(pattern,left))
        right_fil = "".join(re.findall(pattern,right))
        winning_symbol = left_fil
        if left_fil and right_fil and len(left_fil) == len(right_fil):
            winning_symbol=winning_symbol[0]
            if len(left_fil) in range(6, 10):
                print(f'ticket "{el}" - {len(left_fil)}{winning_symbol}')
            elif len(left_fil)  == 10:
                print(f'ticket "{el}" - {len(left_fil)}{winning_symbol} Jackpot!')
        else:
            print(f'ticket "{el}" - no match')
    else:
        print(f'invalid ticket')


