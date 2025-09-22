import sys

input = sys.stdin.readline


def calc(arr):
    temp = 0
    maxSum = arr[0]
    for i in range(len(arr)):
        temp += arr[i]
        if temp > maxSum:
            maxSum = temp

        if temp <= 0:
            temp = 0
    return maxSum


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split(" ")))
    result = calc(arr)
    minResult = calc([-x for x in arr])
    # print(result)
    # print(minResult)
    if result < 0:
        print(0)
    else:
        print(max(result, sum(arr) + minResult))
