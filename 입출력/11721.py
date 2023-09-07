s = input()
start = 0
while(len(s) >= 10):
  print(s[start:start+10])
  s = s[start+10:]
print(s)