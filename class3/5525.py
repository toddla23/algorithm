n = int(input())
m = int(input())
s = input()

a = "I"
for i in range(n):
    a = a + "OI"

count = 0
for i in range(m - len(a) + 1):
    print(s[i : i + len(a)])
    if a == s[i : i + len(a)]:
        count += 1
print(count)
