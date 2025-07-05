class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")
        
    def insert_at_start(self, data):
        new_node = Node(data)
        if not self.head:  
           self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_index(self,data,index):
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
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = temp.next
            temp.next = new_node
            new_node.prev = temp
        
        if new_node.next is None:
            self.tail = new_node    
        
    def delete_by_value(self,val):
        temp  = self.head
        curr = self.head.next            
        
        if self.head.data == val:
            self.head = self.head.next
            self.head.prev = None 
            return
              
        while curr.data != val:
            temp  = curr
            curr  = curr.next 
        if curr:                               
            temp.next = curr.next
            curr.next.prev = temp
            if curr == self.tail:             
                self.tail = temp
                temp.next = None

        else:
            print("target does not exist")
    
    
    def palindrome(self):
        p1  = self.head
        p2  = self.tail
        
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        count = count //2
        if p1 and p2 == None :
            print("List Empty")
            return 
        while count>0:
            if p1.data == p2.data:
                p1 = p1.next
                p2 = p2.prev
                count = count -1 
            else :
                return False    
        return True
            
        
    
    def delete_on_index(self,index):
        if index < 0 :
            print("Index not found")
            return
        temp = self.head
        
        if not temp:
            print("Empty list")
            return
        
        if index == 0:
            self.head = temp.next
            self.head.prev = None       
            return     
        
        pass 
        return

        
dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(10)
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(10)
# dll.display_forward()   
# dll.display_backward()


# dll.insert_at_start(18)
# dll.insert_at_start(25)
# dll.insert_at_start(164)
# dll.display_forward()   
# dll.insert_at_index(18,4)
# dll.display_forward()
# dll.delete_by_value(18)
# dll.display_backward()
dll.display_forward()
# print(dll.palindrome())