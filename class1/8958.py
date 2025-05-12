def answer(s):
  score = 0
  temp = 0
  for i in s:
    if(i == "O"):
      temp = temp + 1
      score = score + temp
    else:
      temp = 0
  print(score)
  return
    

t = int(input())
for i in range(t):
  answer(input())