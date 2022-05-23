ban_word = input().split(", ")
text = input()


for el in ban_word:
    text = text.replace(el,"*"*len(el))
print(text)