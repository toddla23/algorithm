import sys

def push(arr, num):
  arr.append(num)
  return arr

def pop(arr):
  if(len(arr) == 0):
    print(-1)
    return arr
  print(arr.pop())
  return arr

def size(arr):
  print(len(arr))
  return arr

def empty(arr):
  if(len(arr) == 0):
    print(1)
  else:
    print(0)
  return arr

def top(arr):
  if(len(arr) == 0):
    print(-1)
  else:
    print(arr[-1])
  return arr


a = int(sys.stdin.readline())

arr = []
for i in range(a):
  commend = sys.stdin.readline().split()
  if(commend[0] == "push"):
    arr = push(arr, commend[1])
  elif(commend[0] == "pop"):
    arr = pop(arr)
  elif(commend[0] == "size"):
    arr = size(arr)
  elif(commend[0] == "empty"):
    arr = empty(arr)
  elif(commend[0] == "top"):
    arr = top(arr)
  # print(arr)
