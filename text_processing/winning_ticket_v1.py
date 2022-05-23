command =[x.strip() for x in input().split(",")]

winning_set = ['@', '#', '$' , '^']
left =''
right = ''
winning_symbol = ''
for el in command:
    left = el[:int(len(el)/2)]
    right = el[int(len(el)/2):]

    if len(el) == 20:
        winning_symbol = [x for x in winning_set if x in left]
        if winning_symbol:
            winning_symbol = winning_symbol[0]
            win_symb_left = left.count(winning_symbol)
            win_symb_right = right.count(winning_symbol)
            count_left = 1
            count_right = 1
            cont_count_left = 0
            cont_count_right = 0
            for x in range(len(left)-1):
                if left[x] == winning_symbol:
                    if left[x] == left[x+1]:
                        count_left += 1
                        if count_left > 5:
                            cont_count_left == count_left
                            break
                    else:
                        count_left = 1
            for x in range(len(right)-1):
                if right[x] == winning_symbol:
                    if right[x] == right[x+1]:
                        count_right += 1
                        if count_right > 5:
                            cont_count_right ==count_right
                            break
                    else:
                        count_right = 1

        if winning_symbol and win_symb_left in range(6,11):

                if win_symb_left in range(6,10):
                    print(f'ticket "{el}" - {win_symb_left}{winning_symbol}')
                elif win_symb_left == 10:
                    print(f'ticket "{el}" - {win_symb_left}{winning_symbol} Jackpot!')
        else:
            print(f'ticket "{el}" - no match')
    else:
        print("invalid ticket")
