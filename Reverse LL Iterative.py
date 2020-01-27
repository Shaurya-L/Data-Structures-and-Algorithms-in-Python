class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse(head):
    curr = head
    prev = None
    while curr is not None:
        ne_xt = curr.next
        curr.next = prev
        prev = curr
        curr = ne_xt
    head = prev
    return head
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head
def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = reverse(l)
printll(l)
