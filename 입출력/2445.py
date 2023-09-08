t = int(input())

totalLength = t * 2
for i in range(1, t):
  print("*" * i + " " * (totalLength- (i*2)) + "*" * i)

print("*" * totalLength)

for i in range(t-1, 0, -1):
  print("*" * i + " " * (totalLength- (i*2)) + "*" * i)