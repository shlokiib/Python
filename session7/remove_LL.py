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
                        
    def remove_element(self, index):
        if self.head is None:
            print("List is empty")
            return

        # removing element at start
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None  #  empty list
            return

        # removing at a given index
        temp = self.head
        count = 0

        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            print("Index out of bounds")
            return

        to_remove = temp.next
        temp.next = to_remove.next

        # condition last element removed 
        if temp.next is None:
            self.tail = temp

        
        return 
    
    def update_at_index(self, index, new_data):

        # iterating to the index
        temp = self.head
        count = 0
        while temp and count < index:
            temp = temp.next
            count += 1

        # base case
        if temp is None:
            print("Index out of bounds")
            return

        
        temp.data = new_data
        
    def remove_first(self, value):
        if not self.head:
            return      # list is empty 

        
        if self.head.data == value:
            self.head = self.head.next # if first element is value, change head 
            if self.head is None:              
                self.tail = None
            return

        # find first match
        prev  = self.head
        curr = self.head.next
        while curr and curr.data != value:
            prev  = curr
            curr  = curr.next 
        if curr:                               
            prev.next = curr.next
            if curr == self.tail:             
                self.tail = prev

    def remove_all(self, value):
        
        while self.head and self.head.data == value:
            self.head = self.head.next
        if self.head is None:
            self.tail = None
            return

        
        prev, curr = self.head, self.head.next
        while curr:
            if curr.data == value:
                prev.next = curr.next
                if curr == self.tail:          
                    self.tail = prev
                curr = prev.next
            else:
                prev, curr = curr, curr.next
                        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

class Test:
    
    ll = LinkedList()
    for x in [7, 5, 2, 2, 1, 2, 3]:
        ll.insert_at_end(x)

    ll.remove_first(2)     
    ll.display()           

    ll.remove_all(2)      
    ll.display()          
