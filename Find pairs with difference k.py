def number_count(a,b,lst):
    c1=0
    c2=0
    for i in lst:
        if i==a:
            c1+=1
        elif i==b:
            c2+=1
    return c1,c2
def printPairDiffK(l, k):
    n=len(l)
    for i in range(n-1):
        if l[i]+k in l[i+1:] or l[i]-k in l[i+1:]:
            a, b = number_count(l[i]+k,l[i]-k,l[i+1:])
            for j in range(a):
                print(l[i],l[i]+k)
            for j in range(b):
                print(l[i]-k,l[i])
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)
