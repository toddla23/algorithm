import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

answer = deque()


def calc(arr, start, end):
    if start + 1 > end:
        return
    if start + 1 == end:
        print(arr[start])
        return

    root = arr[start]

    cutIdx = end
    for i in range(start + 1, end):
        if arr[i] > root:
            cutIdx = i
            break

    left = calc(arr, start + 1, cutIdx)
    right = calc(arr, cutIdx, end)
    print(root)
    # print(a)
    return


arr = []
while True:
    try:
        t = input()
        arr.append(int(t))
    except:
        break

calc(arr, 0, len(arr))
