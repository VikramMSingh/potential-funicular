class Node:
#Creating a node in the linked list      
    def __init__(self, data):
        #data of the node 
        self.data = data 
        #next pointer
        self.next = None 

class LinkedList:
    def __init__(self): 
    ## initializing the head with None 
        self.head = None 

    def insert(self, new_node):
        ## Check whether the head is empty or not 
        if self.head:
            ## get the last node 
            last_node = self.head
            while last_node.next != None:
                last_node = last_node.next

        ## Assigning the new to the next pointer of last 
            last_node.next = new_node
        else:
            ## head is empty
            ## assign new node to head
            self.head = new_node 

    #iterate through the linked list
    def display(self):
        ## Variable for iteration
        temp_node = self.head
        while temp_node != None:
            ## printing the node data 
            print(temp_node.data, end="->")
            ## moving to the next node
            temp_node = temp_node.next
        print('Null')

if __name__ == '__main__':
    ## instantiating the linked list
    linked_list = LinkedList()
    
