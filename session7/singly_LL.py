class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node   
            self.tail = new_node

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_index(self, data, index):
        if index == 0:
            self.insert_at_start(data)
            return
        
        temp = self.head
        count = 0
        while temp and count < index - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Index out of bounds")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def mid_of_list(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        count = count // 2
        temp = self.head  

        for _ in range(count):
            temp = temp.next

        return temp

    
    
    def rotate__at(self,index):
        temp = self.head
        count = 0 
        while temp.next != self.tail:
            temp = temp.next
        tailtemp = temp.next
        temp = self.head
        while count != index-1:
            count +=1
            temp = temp.next
       
        self.head = temp.next
        self.tail = tailtemp
        return 
               
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")




   
   
ll = LinkedList()

print("Inserting at end:")
for i in range(1,6):
    ll.insert_at_end(i)
    
ll.display


ll.rotate__at(2)
ll.display()