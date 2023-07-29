queuedata = []
front = 0
rear = 0

class Queue:
    def __init__(self, max):
        self.max = max
    def Enqueue(self, data):
        global queuedata
        global front
        global rear
        if(rear < self.max):
            queuedata.append(data)
            rear += 1
            if(not front):
                front = 1
            return 1
        return -1
    def Dequeue(max):
        global queuedata
        global front
        global rear
        temp = None
        if(front):
            temp = queuedata[front - 1]
            if(front > rear):
                front = 0
                rear = 0
                return -1
            else:
                front += 1
        else:
            return -1
        return temp
    def show(max):
        global queuedata
        global front
        global rear
        print(f"\n=== FRONT = {front}, REAR = {rear} ===\n")
        for i in range(rear):
            print(f"{queuedata[i]}\t")
        print("\n")
        
q = Queue(5)
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
q.Enqueue(89)
q.Enqueue(34)
q.Enqueue(66)
q.Enqueue(77)
q.show()
print("\n")
for i in range(rear):
    print(f"{i+1}. Dequeue data {q.Dequeue()}")