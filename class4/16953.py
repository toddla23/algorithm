from collections import deque


a, b = map(int, input().split(" "))

dic = {}
dic[a] = 1
queue = deque([])
queue.append(a)

while queue:
    t = queue.popleft()
    targets = [t * 2, t * 10 + 1]
    for i in targets:
        if 0 < i <=b  and i not in dic.keys():
            dic[i] = dic[t] + 1
            queue.append(i)
            if(i == b):
                break

# print(dic)
print(dic[b] if b in dic.keys() else -1)
