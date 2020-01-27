import queue  #inbuilt stacks and queue
q = queue.Queue(maxsize = 10)  #inbuilt queue
q.put(1)
q.put(2)
q.put(3)
q.put(4)
print(q.qsize())
while not q.empty():
    print(q.get())
q = queue.LifoQueue()  #inbuilt stack
q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get())
