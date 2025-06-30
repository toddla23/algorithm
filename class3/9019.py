import sys
from collections import deque

input = sys.stdin.readline


def dfs(a, b):
    queue = deque([])
    queue.append(a)
    dic = {}
    dic[a] = ''
    while queue:
        a = queue.popleft()
        arr = [
            a * 2 % 10000,
            a - 1 if a > 0 else 9999,
            a % 1000  * 10 + a // 1000,
            a // 10 + a % 10 * 1000,
        ]
        # print(arr)
        for i in range(4):
            calc = "D"
            if i == 1:
                calc = "S"
            elif i == 2:
                calc = "L"
            elif i == 3:
                calc = "R"
                
            if arr[i] == b:
                dic[arr[i]] = dic[a] + calc
                # print(dic)
                return dic[b]
            else:
                if arr[i] not in dic.keys():
                    dic[arr[i]] = dic[a] + calc
                    queue.append(arr[i])


t = int(input())

for i in range(t):
    a, b = map(int, input().split(" "))
    # print(a, b)
    print(dfs(a, b))
