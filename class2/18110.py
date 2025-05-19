import sys

input = sys.stdin.readline
a = 1


def roundUp(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())


arr = []
for i in range(n):
    arr.append(int(input()))


arr.sort()
exc = roundUp(n * 0.15)

# print(arr)
answer = arr[exc : len(arr) - exc]

# print(answer)
# print(sum(answer))

if n == 0:
    print(0)
else:
    print(roundUp(sum(answer) / len(answer)))
