import queue
class StackUsingQueues:
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.count = 0
    def push(self,data):
        self.q1.put(data)
        self.count += 1
    def pop(self):
        if self.count == 0:
            return -1
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        self.count = self.count - 1
        temp=self.q1.get()
        while not self.q2.empty():
            self.q1.put(self.q2.get())
        return temp
    def top(self):
        if self.count == 0:
            return -1
        while self.q1.qsize() != 1:
            self.q2.put(self.q1.get())
        k = self.q1.get()
        while not self.q2.empty():
            self.q1.put(self.q2.get())

        self.q1.put(k)
        return k
    def getSize(self):
        return self.count
s = StackUsingQueues()
li = [int(ele) for ele in input().split()]
i=0
while i<len(li):
    choice = li[i]
    if choice == -1:
        break
    elif choice == 1:
        s.push(li[i+1])
        i+=1
    elif choice == 2:
        ans = s.pop()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 3:
        ans = s.top()
        if ans!=0:
            print(ans)
        else:
            print(-1)
    elif choice == 4:
        print(s.getSize())
    elif choice == 5:
        while s.q1.qsize() !=0:
            print(s.q1.get(),end=' ')           
    i+=1
