k, n = map(int, input().split(" "))

arr = []
for i in range(k):
  arr.append(int(input()))

up = max(arr)
down = 1
mid = (up+down) // 2

while True:
  count = sum([i//mid for i in arr])
  # print(f"down: {down}, up: {up}, mid: {mid}, count:{count}")
  if (down > up):
    print(mid)
    break
  if(count >= n):
    down = mid+1
  if (count < n):
    up = mid-1

  mid = (up+down) // 2
  
  
  
