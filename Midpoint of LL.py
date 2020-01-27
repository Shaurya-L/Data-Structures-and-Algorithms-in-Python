class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def midpoint_linkedlist(head):
    slow = head
    fast = head
    while fast.next and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
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
node = midpoint_linkedlist(l)
if node:
    print(node.data)
