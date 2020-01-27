class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def insertAtIR(head, i, data):
    if i < 0:
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insertAtIR(head.next, i - 1, data)
    head.next = smallHead
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
new_ll = insertAtIR(l, pos, data)
printll(new_ll)
