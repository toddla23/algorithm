def asd(target:int, div:int) -> int:
  result = 0
  while target%div == 0:
    target = target // div
    result = result + 1
  # print(result)
  return result  


n = int(input())
arr = [i for i in range(1, n+1)]

# print(arr)

a= 0
b = 0
for i in arr:
  # print("_________________")
  # print(f"i: {i}")
  if(i % 2 ==0):
    a = a+ asd(i, 2)
  if(i%5 == 0):
    b = b+ asd(i, 5)
  # print("_________________")

    
# print(a, b)
    
print(min(a,b))
