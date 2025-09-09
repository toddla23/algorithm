import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = arr[0]
    min_num = arr[0]
    
    for i in range(1,n):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]
    print(f"{max_num} {min_num}" )
    # print(max(arr), min(arr)) 