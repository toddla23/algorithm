import sys
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    a, b = map(int,input().split(" "))
    arr.append((a, b))
    
asd = sorted(arr, key=lambda x: (x[1],x[0]))

end = 0
answer = []
for i in asd:
    if i[0] >= end:
        answer.append(i)
        end = i[1]
print(len(answer))