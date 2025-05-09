year = int(input())

isyoon = False
if(year % 4 == 0):
  isyoon = True
if (year % 100 == 0):
  isyoon = False
if(year % 400 == 0):
  isyoon = True
  
print(1 if isyoon else 0)