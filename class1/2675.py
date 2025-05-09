t = int(input())
for i in range(t):
  r, s = input().split(" ")
  for j in s:
    for k in range(int(r)):
      print(j, end="")
  print()
    