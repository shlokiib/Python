class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert_at_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node

    def insert_at_index(self, data, index):
               
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1
        
        if not temp:
            print("Index out of bounds")
            return

        node = Node(data)
        node.next = temp.next
        temp.next = node

        if node.next is None:  
            self.tail = node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
