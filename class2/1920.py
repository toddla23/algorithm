n = int(input())
arr = set(map(int, input().split(" ")))
m = int(input())
arr2 = list(map(int, input().split(" ")))

for i in arr2:
  print(1 if i in arr else 0)
