answer = 0
def istwo(num):
  # print(num)
  if(len(num) == 0):
    global answer
    answer = answer + 1
    return

  if(int(num[0:2]) >= 10 and int(num[0:2]) <= 26):
    istwo(num[2:]) 
  istwo(num[1:])


a = input()

istwo(a)
print(answer%1000000)