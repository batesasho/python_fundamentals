command = input().split("\\")
command = command[-1].split(".")
file_name = command[-2]
file_ext = command[-1]

print(f'File name: {file_name}')
print(f'File extension: {file_ext}')
