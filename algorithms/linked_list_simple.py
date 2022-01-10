#Abbreviations: 
#ll - linked list 
#@ - at 
#& - and 

class node:
    def __init__(self,data=None):
        self.data = data
        #data in the node 
        self.next = None  
        #pointer currently initialized @ none 
        #if we have child node we will update next 

class linked_list:
    def __init__(self):
        self.head = None    #blank will not have any data 
    
    def append(self,data):    # add elements to the ll
        new_node = node(data)
        if self.head:
            last_node = self.head
            while last_node.next != None:  #Unless it is the last element of the ll
                last_node = last_node.next
            last_node.next = new_node
        else:
            self.head = new_node
        #Traverse through the ll & create new node @ the end 

    def get_length(self):
        cur = self.head    #Initialize current node @ head of the ll  
        total = 0          #Length = 0 @ beginning 
        while cur.next != None:    #Not @ the end of the list 
            total += 1     #Increment length by 1 
            cur = cur.next #Move current node to next node till it reaches last node 
        print(total)
        return total

    def display(self):
        #elems = []    #Initialize a list
        cur = self.head   #Initialize current node @ head of the ll 
        while cur != None:
            print(cur.data, end="->")
            cur = cur.next
        print("Null")
        

    def get_element(self, index): #Index to specify the node we want 
        #Check index in range
        if index >= self.get_length():
            print("Error: Index out of range")
            return None 
        cur_index = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_index == index:
                return cur_node.data 
            cur_index += 1 
    
    def delete_node(self,index):
        #Check index in range
        if index >= self.get_length():
            print("Error: Index out of range")
            return None 
        cur_index = 0
        cur = self.head
        while cur != None:
            last_node = cur           #Initialize pointer @ head
            if index == 0:
                self.head = cur.next  #Move head to next node 
                last_node = None      #Delete the next node 
                return
            elif index == cur_index:   
                cur = last_node.next     #Move cur pointer to next
                p = last_node.next
                last_node.next = cur.next #Skip over the node we are deleting
                print(f"Deleting node {p} with value {p.data}")
                p = None  
                return 
            cur_index += 1

    def reverse(self):
        cur = self.head
        foll = self.head
        prev = None 
        while cur != None:
            foll = foll.next
            cur.next = prev
            prev = cur
            cur = foll
        self.head = prev
    
    def sum_linked(self):
        cur = self.head
        sum_ll = 0 
        while cur != None:
            sum_ll += cur.data
            cur = cur.next 
        print(sum_ll) 

    def max_val(self):
        cur = self.head
        max_val = -32678
        while cur != None:
            if cur.data > max_val:
                max_val = cur.data
            cur = cur.next
        print(max_val)

    def count_ll(self):
        cur = self.head
        count = 0 
        while cur != None:
            count += 1
            cur = cur.next
        print(count)
    
    def search(self, value):
        cur = self.head
        while cur != None:
            if cur.data == value:
                print(cur) 
                break; 
            cur = cur.next
        print(cur)

if __name__ == "__main__":
    linked_list = linked_list()