class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverseRecursive(head):
    if head is None:
        return None
    if head.next is None:
        return head
    small_head = reverseRecursive(head.next)
    tail_ll = head.next
    tail_ll.next = head
    head.next = None
    return small_head
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
from sys import setrecursionlimit
setrecursionlimit(11000)
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)

