n, c, r = map(int, input().split(" "))
# print(n, c, r)

# c -= 1
# r -= 1
l = 2**n

# print(l)

arr = []
while l >= 2:
    if l // 2 > c and l // 2 > r:
        arr.append(0)
    elif l // 2 > c and l // 2 <= r:
        arr.append(1)
        r = r - l // 2
    elif l // 2 <= c and l // 2 > r:
        arr.append(2)
        c = c - l // 2
    else:
        arr.append(3)
        r = r - l // 2
        c = c - l // 2
    l = l // 2

answer = 0
for i in range(len(arr)):
    answer = answer + 4**(len(arr) - i - 1) * arr[i]
# print(arr)
print(answer)
