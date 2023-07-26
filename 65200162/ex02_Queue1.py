max = 11
queuedata = []
front = 0
rear = 0

def add(data):
    global front
    global rear
    if(rear < max + 1):
        rear += 1
        queuedata.append(data)
        if(not front):
            front = 1
        return 1
    return -1

def get():
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

add(5)
add(6)
add(7)
add(8)
add(9)
add(10)
add(11)
add(12)
add(13)
print(f"add result = {add(14)}")
print(f"add result = {add(82)}")

show()
print("\n")
for i in range(rear):
    print(f"{i+1}. get data = {get()}")