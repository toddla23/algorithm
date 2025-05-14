N, K = map(int,input().split(""))
index = 0
array = list(range(1,N+1))
result = []

while len(array) != 0:
    index += (K-1)
    index = index % len(array)
    result.append(array.pop(index))

## 문자
print("<",end="")
for i in range(N-1):
    print(result[i],end=", ")
print(result[N-1], end = "")
print(">",end="")