t = int(input())
for i in range(1,t + 1):
  a, b = map(int, input().split(" "))
  print("Case #"+str(i) + ": " + str(int(a)+int(b)))