import sys

input = sys.stdin.readline


n, m = map(int, input().split(" "))

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split(" "))))

prefixSum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# print(prefixSum)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefixSum[i][j] = (
            prefixSum[i][j - 1]
            + arr[i - 1][j - 1]
            + prefixSum[i - 1][j]
            - prefixSum[i - 1][j - 1]
        )

# for i in prefixSum:
#     print(i)

for _ in range(m):
    a, b, c, d = list(map(int, input().rstrip().split(" ")))
    print(prefixSum[c][d] - prefixSum[c][b-1] - prefixSum[a-1][d] + prefixSum[a-1][b-1] )
