import sys

input = sys.stdin.readline

n, m, b = map(int, input().split(" "))

arr = []
for _ in range(n):
    arr.extend(list(map(int, input().split(" "))))


answer = []
s = []
for i in range(256 + 1):
    stock = b
    temp = 0
    for j in arr:
        if j < i:
            temp += 1 * (i - j)
            stock -= i - j
        elif j > i:
            temp += 2 * (j - i)
            stock += j - i
    s.append(stock)
    answer.append(temp)

a = answer[0]
hight = 0
for i in range(len(answer)):
    if answer[i] <= a and s[i] >= 0:
        a = answer[i]
        hight = i


print(a, hight)
