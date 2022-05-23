seq = list(map(int, input().split(", ")))
index_start = int(input())
type_items = input()

right = seq[:index_start]
left = seq[index_start + 1:]
new_right = []
new_left = []

if type_items == "expensive":
    new_right = [right[x] for x in range(len(right)) if right[x] >= seq[index_start]]
    new_left = [left[x] for x in range(len(left)) if left[x] >= seq[index_start]]
else:
    new_right = [right[x] for x in range(len(right)) if right[x] < seq[index_start]]
    new_left = [left[x] for x in range(len(left)) if left[x] < seq[index_start]]

if sum(new_left) > sum(new_right):
    print(f"Right - {sum(new_left)}")
else:
    print(f"Left - {sum(new_right)}")
