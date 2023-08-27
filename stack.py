class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.length = 1
    def push(self, value):
        newNode = Node(value)
        if(self.length == 0):
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.length += 1
        return self
    def pop(self):
        if(self.length == 0):
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -= 1
            return temp