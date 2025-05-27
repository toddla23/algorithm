n = int(input())
arr = list(map(int, input().split(" ")))


arr.sort()
# print(n)
# print(arr)
answer = 0
for i in range(len(arr)):
    answer = answer + sum(arr[: i + 1])
    # print(arr[: i + 1])
    # print(sum(arr[: i + 1]))
print(answer)
