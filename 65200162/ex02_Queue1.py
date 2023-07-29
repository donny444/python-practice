max = 11
queuedata = []
front = 0
rear = 0

def Enqueue(data):
    global front
    global rear
    if(rear < max):
        queuedata.append(data)
        rear += 1
        if(not front):
            front = 1
        return 1
    return -1

def Dequeue():
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

def show():
    print(f"\n=== FRONT = {front}, REAR = {rear} ===\n")
    for i in range(rear):
        print(f"{queuedata[i]}\t")
    print("\n")

Enqueue(5)
Enqueue(6)
Enqueue(7)
Enqueue(8)
Enqueue(9)
Enqueue(10)
Enqueue(11)
Enqueue(12)
Enqueue(13)
print(f"Enqueue result = {Enqueue(14)}")
print(f"Enqueue result = {Enqueue(82)}")
print(f"Enqueue result = {Enqueue(66)}")
print(f"Enqueue result = {Enqueue(77)}")

show()
print("\n")
for i in range(rear):
    print(f"{i+1}. Dequeue data = {Dequeue()}")