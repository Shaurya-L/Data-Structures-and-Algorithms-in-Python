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
def delete(head, i):
    if i < 0 or i >= length(head):
        return head
    count =  0
    prev = None
    curr = head
    curr_next = None
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    if i == 0:
        head = curr.next
        return head
    curr_next = curr.next
    prev.next = curr_next
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
i=int(input())
l = delete(l, i)
printll(l)
