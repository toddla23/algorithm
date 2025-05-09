import math
def carculate( x, y, c):
  # print(c%x)
  # print(math.ceil(c/x))
  print(f"{c%x if c%x != 0 else x}{format(math.ceil(c/x),"02")}")
  


t = int(input())
for i in range(t):
  x, y, c = map(int, input().split(" "))
  carculate(x, y, c)
