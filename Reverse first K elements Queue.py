import queue
def reverseQueue(q, k):
    if k<=0 or q.qsize()<=1:
        return
    ele=q.get()
    reverseQueue(q,k-1)
    q.put(ele)
    return    
def reverseFirstK(q,k):
    reverseQueue(q,k)
    n=q.qsize()
    for i in range(n-k):
        q.put(q.get())
from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
li = [int(ele) for ele in input().split()]
q = queue.Queue()
for ele in li:
	q.put(ele)
k = int(input())
reverseFirstK(q,k) 
while(q.qsize()>0):
	print(q.get())
	n-=1
