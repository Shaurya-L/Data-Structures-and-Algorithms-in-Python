class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def length(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count
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
len=length(l)
print(len)

"""
def lengthRecursive(head):
    if head is None:
        return 0
    return 1 + lengthRecursive(head.next)
"""
