class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def kReverse(head, n) :
    if(head is None ):
        return None
    prev=None 
    curr=head
    next=None 
    count=0
    while(curr is not None and count<n):
        next=curr.next
        curr.next=prev
        prev=curr
        curr=next
        count+=1
    head.next=kReverse(curr,n)
    return prev

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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
l = kReverse(l, i)
printll(l)
