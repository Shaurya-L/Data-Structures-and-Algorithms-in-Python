class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def linearSearch(head, n):
    count = 0
    while head is not None:
        if n == head.data:
            return count
        count = count + 1
        head = head.next
    return -1
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
data=int(input())
index = linearSearch(l, data)
print(index)
