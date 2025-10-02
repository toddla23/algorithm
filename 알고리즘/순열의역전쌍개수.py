import sys

input = sys.stdin.readline

answer = 0


def mearge(arr, start, mid, end):
    global answer
    print(start, mid, end)

    a = start
    b = mid + 1
    t = 0
    temp = [0 for _ in range(end - start + 1)]
    # print(f"temp: {temp}")
    while a <= mid and b <= end:
        if arr[a] <= arr[b]:
            temp[t] = arr[a]
            a += 1
            t += 1
        else:
            temp[t] = arr[b]
            b += 1
            t += 1
            answer += mid + 1 - a
        # print(arr)

    while a <= mid:
        temp[t] = arr[a]
        a += 1
        t += 1
    while b <= end:
        temp[t] = arr[b]
        b += 1
        t += 1
    # print(temp)

    for i in range(end - start + 1):
        arr[start + i] = temp[i]
    # print(f"arr: {arr}, answer: {answer}")
    return temp


def devide(arr, start, end):
    mid = (start + end) // 2
    if end - start == 0:
        return
    devide(arr, start, mid)
    devide(arr, mid + 1, end)
    mearge(arr, start, mid, end)
    return


t = int(input())

for _ in range(t):
    answer = 0
    n = int(input())
    arr = list(map(int, input().split(" ")))
    devide(arr, 0, len(arr) - 1)
    print(answer)
