text = input()
command = input()

while not command == "Done":
	command = command.split()
	if command[0] == "TakeOdd":
		text = ''.join([text[x] for x in range(len(text)) if not x % 2 == 0])
		print(text)
	elif command[0] == "Cut":
		text = text[:int(command[1])] + text[int(command[1])+int(command[2]):]
		print(text)
	elif command[0] == "Substitute":
		if command[1] in text:
			text = text.replace(command[1],command[2])
			print(text)
		else:
			print("Nothing to replace!")
	command = input()
else:
	print(f"Your password is: {text}")

