import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

low = 0
high = max(arr)
result = 0

while low <= high:
    cutter_length = (low + high) // 2
    getted_tree = sum(i - cutter_length for i in arr if i > cutter_length)
    if getted_tree >= m:
        result = cutter_length
        low = cutter_length + 1
    else:
        high = cutter_length - 1

print(result)
