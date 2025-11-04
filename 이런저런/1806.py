import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))


temp = 0

start = 0
end = -1
length = float('inf')

a1 = 0
for i in range(len(arr)):
    a1 = a1 + arr[i]
    start = i

    # print(f"a1: {a1}")
    if a1 >= s:
        length = min(length, start - end)
        for j in range(end+1, i):
            end = j
            a1 = a1 - arr[j]
            if a1 >= s:
                length = min(length, start - end)
                # print(f"delete a2: {a1}, start: {start}, end: {end}, length:{length}")
            else:
                break

    # print(f"final a1:{a1} start: {start}, end: {end}, length:{length}")
if length == float("inf"):
    print(0)
else:
    print(length)