t = int(input())

answerArr = [0 for i in range(31)]
answerArr[2] = 3
answerArr[4] = 12


for i in range(3, t+1):
  if(i % 2 == 1):
    answerArr[i]  = 0
  else:
    temp = 0
    for j in range(1, i-2):
      if j % 2 == 0:
        temp = temp + answerArr[j]
    answerArr[i] = 3 * answerArr[i-2] + 2 * (temp) + 2

print(answerArr[t])
  