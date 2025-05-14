def getAnswer(num:int) -> str:
  if(num%3 == 0 and num % 5 == 0):
    return "FizzBuzz"
  elif(num%3 == 0 and num % 5 != 0):
    return 'Fizz'
  elif(num%3 !=0 and num % 5 == 0):
    return "Buzz"
  return str(num)
  
  

a = input()
b = input()
c = input()

fizz = 'Fizz'

if(a.isnumeric()):
  print(getAnswer(int(a)+3))
elif(b.isnumeric()):
  print(getAnswer(int(b)+2))
elif(c.isnumeric()):
  print(getAnswer(int(c)+1))
