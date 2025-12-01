import sys

input = sys.stdin.readline


def calc(weight, stuff):
    values = [[0 for _ in range(weight+1)] for _ in range(len(stuff) + 1)] # values[stuff][weight]
    
    for i in range(len(stuff)):
        stuffWeight, stuffValue = stuff[i]
        print(stuffWeight, stuffValue)
        for j in range(1, weight+1):
            if stuffWeight > j:
                values[i][j] = values[i-1][j]
            else:
                value1 = values[i-1][j] # 나 없을떄의 최대값
                value2 = values[i-1][j-stuffWeight] + stuffValue # 나 있을때 최대값
                values[i][j] = max(value1, value2)
        for k in values:
            print(k)
        print("________________________________")

    
    return values[len(stuff)-1][weight]


n, k = list(map(int, input().split(" ")))

arr = []
for i in range(n):
    w, v = list(map(int, input().split(" ")))
    arr.append([w, v])

result = calc(k, arr)
print(result)
