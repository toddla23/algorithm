import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split(" "))))


for i in range(n):
    for j in range(n):
        for k in range(n):
            if arr[j][k] != 1:
                arr[j][k] = 1 if (arr[j][i] * arr[i][k]) > 0 else 0
    # for a in arr:
    #     print(a)
    # print("________________________")

            
for i in arr:
    print(" ".join(list(map(str,i))))