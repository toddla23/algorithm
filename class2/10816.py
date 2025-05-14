n = int(input())
n_arr = input().split(" ")
m = int(input())
m_arr = input().split(" ")

dic = {}
for i in n_arr:
  if i not in dic.keys():
    dic[i] = 1
  else:
    dic[i] += 1

answer = []
for i in m_arr:
  if i not in dic.keys():
    answer.append(0)
  else:
    answer.append(dic[i])
print(" ".join([ str(i) for i in answer]))

