arr = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

m, d = map(int, input().split(" "))

thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
twentyEight = [2]

answer = 0
for i in range(1, m):
  if(i in thirty):
    answer = answer + 2
  elif(i in thirtyOne):
    answer = answer + 3
  else:
    answer = answer

print(arr[(answer + d) % 7])