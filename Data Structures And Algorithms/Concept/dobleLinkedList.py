
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        # self.tail =None

    def addEnd(self, data):
        new_node = Node(data)
        n = self.head
        if n == None:
            self.head = new_node
            #self.head.previous = self.tail.next_node = None
        else:
            # self.tail.next_node = new_node
            # new_node.previous = self.tail
            while n is not None:
                n = n.next_node
            n = new_node

    def addBegin(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def printdoubleLinkedList(self):
        if self.head == None:
            print('List is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" ")
                n = n.next_node


l = DoubleLinkedList()
l.printdoubleLinkedList()
l.addBegin(10)
# l.addBegin(20)
l.addBegin(30)
l.printdoubleLinkedList()
