seq = input()
new = ''
explosion = 0
offset = 0

while ">" in seq:
    current_mark =seq.find('>')
    explosion += int(seq[current_mark + 1])
    new += seq[:current_mark+1]
    seq = seq[current_mark + 1:]
    offset = seq.find('>')
    if offset <0:
        seq = seq[explosion:]
        new += seq[:]
    elif explosion <= offset:
        seq = seq[explosion:]
        explosion = 0
    elif explosion > offset:
        explosion -= offset
        seq = seq[offset:]
else:
    print(new)