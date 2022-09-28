class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        n = self.head
        if n == None:
            print('List is empty')
        while n is not None:
            print(n.data, end=" ")
            n = n.ref

    def addBeg(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def addafter(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n == None:
            print(x, 'data not in List ')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def delBeg(self):
        self.head = self.head.ref

    def delEnd(self):
        n = self.head
        if n == None:
            print('List is empty cant perform del')
            return 0
        elif n.ref == None:
            n = None
        else:
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
