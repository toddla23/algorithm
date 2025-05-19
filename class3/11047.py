import sys

input = sys.stdin.readline

n, k = map(int, input().split(" "))
# print(n, k)

arr = []
for _ in range(n):
    arr.append(int(input()))

answer = 0
# answer = []
while k > 0:
    target = arr[-1]
    # print(k)
    if target <= k:
        # answer.append(target)
        # answer.append(k // target)
        answer += k // target
        k = k % target
    else:
        arr.pop()

print(answer)
# print(sum(answer))
