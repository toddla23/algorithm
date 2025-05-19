import sys
input = sys.stdin.readline

m = int(input())

bucket = set()
# answer = []
for _ in range(m):
  a = list(input().split())
  if(a[0] == 'add'):
    bucket.add(int(a[1]))
  elif(a[0] == 'remove'):
    bucket.discard(int(a[1]))
  elif(a[0] == 'check'):
    # answer.append(1) if int(a[1]) in bucket  else answer.append(0)
    print(1 if int(a[1]) in bucket else 0)
  elif(a[0] == 'toggle'):
    bucket.discard(int(a[1])) if int(a[1]) in bucket else bucket.add(int(a[1]))
  elif(a == 'all'):
    print(123123)
    bucket = set([i for i in range(1, 21)])
  else:
    bucket = set()
  # print(a[0])
  print(bucket)
    
