arr = list(map(int, input().split(" ")))
x = 0
for i in arr:
  x += i**2
print(x%10)