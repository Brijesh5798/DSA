class Node:
    def __init__(self,data=None,next=None,previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def print(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
        
    def insert_at_begining(self,data):
        if self.head is None:
            node = Node(data,self.head)
            self.head = node
            self.tail = node
            return
        node = Node(data,self.head)
        self.head.previous = node
        self.head = node
        
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data,None,self.head)
            self.head = node
            self.tail = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        node = Node(data,None,itr)
        itr.next = node
        self.tail = node
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        print(self.get_length(),"length")
        if index < 0 or index > self.get_length():
            raise Exception("wrong index")
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.previous = None 
            return
        if index == self.get_length() -1:
            print("removig last")
            self.tail = self.tail.previous
            self.tail.next = None
            return
        count = 0
        itr = self.head
        while count <= index:
            if count == index - 1:
                itr.next = itr.next.next
                itr.next.previous = itr
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("wrong index")
        if index == 0:
            # self.head = Node(data,self.head)
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next,itr)
                itr.next.previous = node
                itr.next = node
                break
            itr = itr.next
            count += 1
            
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count =  0
        while itr:
            if itr.data == data_after:
                self.insert_at(count + 1 ,data_to_insert)
                return
            count += 1
            itr = itr.next
            
    def remove_by_value(self, data):
        itr = self.head
        count =  0
        print(itr.data,"itr data")
        while itr:
            if itr.data == data:
                print(count,"count")
                self.remove_at(count)
                return
            count += 1
            itr = itr.next
            
    def print_forward(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)
    
    def print_backward(self):
        if self.head is None:
            print("list is empty")
            return
        itr = self.tail
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.previous
        print(llstr)
        
if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.print_backward()
    ll.print_forward()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()