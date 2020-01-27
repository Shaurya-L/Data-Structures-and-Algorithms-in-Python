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
def insertAtI(head, i, data):
    if i < 0 or i > length(head):
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
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
data = int(input())
pos = int(input())
new_ll = insertAtI(l, pos, data)
printll(new_ll)
