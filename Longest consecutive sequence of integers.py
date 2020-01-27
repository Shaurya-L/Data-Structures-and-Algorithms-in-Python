def longestConsecutiveSubsequence(l):
    m=max(l)
    lst=[-1]*(m+1)
    for ele in l:
       lst[ele]=ele
    maxVal=0
    maxIndex=0
    for i in range(m+1):
        temp=0
        while i<=m and lst[i]!=-1:
            temp+=1
            i+=1
        else:
            i-=1
        if temp>=maxVal:
            if temp==maxVal and temp!=0:
                tIndex=i-temp+1
                if l.index(lst[tIndex])<l.index(lst[maxIndex]):
                    maxVal=temp
                    maxIndex=i-temp+1
            else:
                maxVal=temp
                maxIndex=i-temp+1
    final=lst[maxIndex:maxIndex+maxVal]
    return final
#Implement Your Code Here
#You have To Return the list of longestConsecutiveSubsequence


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
final = longestConsecutiveSubsequence(l)
for num in final:
    print(num)
