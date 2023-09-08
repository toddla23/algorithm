t = int(input())

for i in range(1, t):
  print(" "* (t-i) + "*" * (i))

print("*" * t)

for i in range(t-1, 0, -1):
  print(" "* (t-i) + "*" * (i))
