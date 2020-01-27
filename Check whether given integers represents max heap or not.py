import heapq
def checkMaxHeap(lst):
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    maxIndex=len(lst)-1
    flag=True
    for i in range(maxIndex):
        c1=2*i+1
        c2=2*i+2
        l=-100000
        r=-100000
        if c1<=maxIndex:
            l=lst[c1]
        if c2<=maxIndex:
            r=lst[c2]
        maximum=max(l,r)
        if maximum>lst[i]:
            flag=False
            break
    return flag

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')
