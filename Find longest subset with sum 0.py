def subsetSum(l):
#Implement Your Code Here
    d = {} 
    max_len = 0
    curr_sum = 0
    for i in range(n): 
        curr_sum += l[i] 
        if l[i]==0 and max_len == 0: 
            max_len = 1
        if curr_sum is 0: 
            max_len = i + 1
        if curr_sum in d: 
            max_len = max(max_len, i - d[curr_sum] ) 
        else:  
            d[curr_sum] = i 
  
    return max_len 
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
finalLen= subsetSum(l)
print(finalLen)
