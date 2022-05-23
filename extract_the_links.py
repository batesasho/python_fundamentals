import re

link = input()
pattern =r'www\.[A-Za-z0-9-]+(\.[a-z]+)+'

while link:
    processed_link = re.finditer(pattern,link)
    [print(x.group()) for x in processed_link]

    link = input()