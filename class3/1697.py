from collections import deque

n, k = map(int, input().split(" "))

time = 0
time_limit = k - n

arr = [0 for i in range(100001)]

queue = deque()
queue.append(n)

arr[n] = 1

while queue:
    a = queue.popleft()

    if a == k:
        print(arr[a] - 1)  # 결과 출력 시 -1 보정
        break

    if a + 1 <= 100000 and arr[a + 1] == 0:
        arr[a + 1] = arr[a] + 1
        queue.append(a + 1)
    if a - 1 >= 0 and arr[a - 1] == 0:
        arr[a - 1] = arr[a] + 1
        queue.append(a - 1)
    if a * 2 <= 100000 and arr[a * 2] == 0:
        arr[a * 2] = arr[a] + 1
        queue.append(a * 2)
