import sys

input = sys.stdin.readline


def kadane(arr: list) -> int:
    tempSum = 0
    maxSum = 0
    a, b = -1, -1
    
    temp = 0
    
    for i in range(len(arr)):
        tempSum = tempSum + arr[i]
        if tempSum > maxSum:
            maxSum = tempSum
            a = temp
            b = i
        elif tempSum <= 0:
            tempSum = 0
            temp = i + 1
        # print(f"i: {i}, {tempSum}, {maxSum}, {a}, {b}")
    print(f"{maxSum} {a} {b}")

    return maxSum


t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    kadane(arr[1:])
