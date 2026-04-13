def insert(heapq, item):
    heapq.append(item) # [9, 8, 7, 10]
    itemSpot = len(heapq) - 1 # 1
    while item > heapq[itemSpot // 2] and itemSpot > 0: # 10 > 9
        heapq[itemSpot] = heapq[itemSpot // 2] # [9,9,7,8]
        itemSpot = itemSpot // 2 # 0
   
    heapq[itemSpot] = item
    print(heapq)
    print("________") 
    return heapq
        

heapq = [456]
answer = []
insert(heapq, 9)
insert(heapq, 8)
insert(heapq, 7)
insert(heapq, 10)
