import  heapq

def timeTaken(lst,myPriority):
    Priority=lst[myPriority]
    heapq._heapify_max(lst)
    time=0
    while True:
       # print(lst)
        temp=heapq._heappop_max(lst)
        time+=1
        if temp==Priority:
            return time

n=int(input())
lst=[int(x) for x in input().split()]
myPriority=int(input())
print(timeTaken(lst,myPriority))
