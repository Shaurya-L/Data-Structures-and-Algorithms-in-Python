class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def lengthLL(head):
    count = 0
    while head is not None:
        count = count + 1
        head = head.next
    return count
def append_LinkedList(head,n) :
    count = lengthLL(head) - n 
    i=1
    curr=head
    while(i < count):
        curr=curr.next
        i += 1
        
    head2 = curr.next
    curr.next = None
    
    tail = head2
    i = 0
    while tail.next is not None :
        tail = tail.next
    tail.next = head
    return head2
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
l = append_LinkedList(l, i)
printll(l)
