queuedata = []
front = 0
rear = 0

class Queue:
    def __init__(self, max):
        self.max = max
    def add(self, data):
        global queuedata
        global front
        global rear
        if(rear < self.max + 1):
            rear += 1
            queuedata.append(data)
            if(not front):
                front = 1
            return 1
        return -1
    def get(max):
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
q.add(1)
q.add(2)
q.add(3)
q.add(89)
q.add(34)
q.show()
print("\n")
for i in range(rear):
    print(f"{i+1}. get data {q.get()}")