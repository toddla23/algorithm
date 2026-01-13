n = int(input())
arr = [[]]
for i in range(n):
    a, b = list(map(int, input().split()))
    arr.append((a, b))

answer = [0] * (n + 1)
for i in range(1, n + 1):
    a, b = arr[i]
    for j in range(i, n + 1):
        if (j + a - 1) > n:
            continue
        answer[(j + a - 1)] = max(answer[i-1] + b, answer[(j + a - 1)])
print(answer[-1])
