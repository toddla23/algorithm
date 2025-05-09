n, x = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

answer = []
for i in arr:
  if(i < x):
    answer.append(i)
print(" ".join([str(i) for i in answer]))