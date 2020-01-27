import heapq
def kthLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    n = len(lst)
    for i in range(k, n):
        if heap[0] < lst[i]:
            heapq.heapreplace(heap, lst[i])
    k = heapq.heappop(heap)
    print(k)
n = int(input())
lst = list(int(i) for i in input().strip().split(' '))
k = int(input())
kthLargest(lst, k)
