import sys
a = int(sys.stdin.readline())

dic = {}
for i in range(a):
  b = int(sys.stdin.readline())
  if(b not in dic):
    dic[b] = 1
  else:
    dic[b] = dic[b] + 1


for i in sorted(dic):
  for j in range(dic[i]):
    print(i)