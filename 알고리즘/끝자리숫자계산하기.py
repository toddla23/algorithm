import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    answer = 1
    for i in arr[1:]:
        answer = ((i%10)*answer)%10
    
    print(answer)