import math as math
n = int(input())
orders = list(map(int,input().split(" ")))
t, p = map(int, input().split(" "))

a = 0
for i in orders:
  # a = a + i // t if i%p == 0 else i//t+1
  # print(math.ceil(i/t))
  a = a+ math.ceil(i/t)

print(a)
print(n//p, n%p)