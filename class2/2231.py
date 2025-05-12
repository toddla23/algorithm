n = int(input())

a = 0

for i in range(n-54 if n-54 > 0 else 1, n+1):
  arr = list(map(int,str(i)))
  # print(arr)
  if(sum(arr) + i == n):
    # print(i)
    a = i
    break
print(a)

