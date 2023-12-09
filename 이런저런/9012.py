a = int(input())

for i in range(a):
  x = input()
  b = 0
  for j in range(len(x)):
    if(b < 0):
      break
    if(x[j] == '('):
      b = b + 1
    else:
      b = b - 1
  if(b == 0):
    print("YES")
  else:
    print("NO")