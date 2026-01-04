import itertools


 

n, m = list(map(int, input().split(" ")))

home = []
store = []
for i in range(n):
    temp = list(map(int, input().split(" ")))
    for j in range(n):
        if temp[j] == 1:
            home.append((i + 1, j + 1))

        elif temp[j] == 2:
            store.append((i + 1, j + 1))
            
            

# print(home)
# print(store)
pool = [ i for i in range(len(store))]
storeComb = list(itertools.combinations(pool,m))
# print(storeComb)
minAnswer = float('inf')
for i in range(len(storeComb)):
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    storeList = list(storeComb[i])
    tempAnswer = 0
    for j in range(len(home)):    
        tempDistance = float("inf")
        for k in range(len(storeList)):
            tempDistance = min(tempDistance, abs(home[j][0] -store[storeList[k]][0]) + abs(home[j][1] - store[storeList[k]][1]))
        # print(home[j], tempDistance)
        tempAnswer += tempDistance
    
    # print(tempAnswer)
    minAnswer = min(minAnswer, tempAnswer)
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(minAnswer)