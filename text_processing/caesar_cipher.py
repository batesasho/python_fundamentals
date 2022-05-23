command = input()

new = ''

for letter in command:
    new += chr(ord(letter)+3)
print(new)