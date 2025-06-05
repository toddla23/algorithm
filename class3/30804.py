n = int(input())
arr = list(map(int, input().split(" ")))

count = {}
start = 0
max_len = 0

for end in range(n):
    fruit = arr[end]
    if fruit in count:
        count[fruit] += 1
    else:
        count[fruit] = 1

    while len(count) > 2:
        left_fruit = arr[start]
        count[left_fruit] -= 1
        if count[left_fruit] == 0:
            del count[left_fruit]
        start += 1

    max_len = max(max_len, end - start + 1)

print(max_len)
