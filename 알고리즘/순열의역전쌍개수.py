import sys

input = sys.stdin.readline

answer = 0


def mearge(arr, start, mid, end):
    global answer
    # print(start, mid, end)

    a = start
    b = mid + 1
    t = start
    temp = arr[:]
    # print(f"temp: {temp}")
    while a <= mid and b <= end:
        if temp[a] <= temp[b]:
            arr[t] = temp[a]
            a += 1
            t += 1
        else:
            arr[t] = temp[b]
            b += 1
            t += 1
            answer += mid+1 - a
        # print(arr)

    while a <= mid:
        arr[t] = temp[a]
        a += 1
        t += 1
    while b <= end:
        arr[t] = temp[b]
        b += 1
        t += 1
    # print(temp)
    # print(f"arr: {arr}, answer: {answer}")
    return temp


def calc(arr, start, end):
    mid = (start + end) // 2
    if end - start == 0:
        return
    calc(arr, start, mid)
    calc(arr, mid + 1, end)
    mearge(arr, start, mid, end)
    return


t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split(" ")))
    calc(arr, 0, len(arr) - 1)
    print(answer)
