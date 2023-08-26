class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__ (self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = self.head
        self.length = 1
    def push(self, value):
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self
    def pop(self):
        if(self.length == 0): return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if(self.length == 0):
            self.head = None
            self.tail = None
        return temp
    def unshift(self, value):
        newNode = Node(value)
        if(not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self
    def shift(self):
        if(self.length == 0): return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if(self.length == 0):
            self.tail = None
        temp.next = None
        return temp

LinkedList.push(1)
LinkedList.push(2)
LinkedList.push(3)