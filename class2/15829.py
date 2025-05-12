n = int(input())


l = list(map(ord, input()))
arr = [i-96 for i in l]
# print(arr)
a = 0
for i in range(len(arr)):
  a = (a + 31**i * (arr[i]))%1234567891
print(a)