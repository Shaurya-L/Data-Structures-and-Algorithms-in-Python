def maxFreq(l): 
    map = {} 
    for num in l: 
        if num in map: 
            map[num] += 1 
        else: 
            map[num] = 1 
    ans = l[0] 
    for num in l: 
        if map[num] > map[ans]: 
            ans = num 
    return ans 
n=int(input()) 
l=list(int(i) for i in input().strip().split(' ')) 
print(maxFreq(l))
