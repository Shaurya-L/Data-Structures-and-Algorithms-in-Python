n = int(input())
price = [int(ele) for ele in input().split()]
lst1 = [1]
count = 0
for i in range(1, len(price)):
    for j in range(i - 1, -1, -1):
        if price[i] > price[j]:
            count = count + 1
        else:
            break
    count = count + 1
    lst1.append(count)
    count = 0
print(*lst1)
