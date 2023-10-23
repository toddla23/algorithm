def fuc(l, arr):
  answerArray = [[0 for i in range(l)] for j in range(2)]

  answerArray[0][0] = arr[0][0]
  answerArray[1][0] = arr[1][0]

  for i in range(1, l):
    answerArray[0][i] = answerArray[1][i-1] + arr[0][i] if answerArray[1][i-1] > answerArray[1][i-2] else answerArray[1][i-2] + arr[0][i]
    answerArray[1][i] = answerArray[0][i-1] + arr[1][i] if answerArray[0][i-1] > answerArray[0][i-2] else answerArray[0][i-2] + arr[1][i]
  
  # print(answerArray)
  return max(answerArray[0][l-1], answerArray[1][l-1])


t = int(input())
for n in range(t):
  l = int(input())
  arr = [[0 for i in range (l)] for j in range(2)]
  arr[0] = list(map(int, input().split(" ")))
  arr[1] = list(map(int, input().split(" ")))

  if l == 1:
    print(max(arr[0][0], arr[1][0]))
  elif l == 2:
    print(max(arr[0][0] + arr[1][1], arr[1][0] + arr[0][1]))
  else: 
    print(fuc(l, arr))
