import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    f = list(input().rstrip())
    n = int(input())
    a = input().rstrip()
    arr = deque(list(map(int, a[1 : len(a) - 1].split(","))) if len(a) >= 3 else [])

    e = 0
    r = 0
    for j in f:
        if j == "R":
            r += 1
        else:
            if len(arr) == 0:
                print("error")
                e = 1
                break
            else:
                if r % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()

    if e == 0:
        if r % 2 == 1:
            arr.reverse()
            
        
        print("[" + ",".join(map(str,list(arr)))+"]")
