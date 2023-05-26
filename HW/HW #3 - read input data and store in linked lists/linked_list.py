# Create a Node
class GetNode:
    def __init__(self, info, next_node=None):
        self.info = info
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

# Singly Linked List (Queue)
class FIFO:
    def __init__(self):
        # define pointers 
        self.head = None
        self.rear = None
    
    # adding to the end (First in)
    def add_to_rear(self, info):
        new_node = GetNode(info)

        # check if the queue is empty
        if self.head == None and self.rear == None:
            # set both pointers to a node
            self.head = new_node
            self.rear = new_node
        # otherwise the list has at least first item head pointer
        else:
            # assign existing node's next node
            self.rear.set_next_node(new_node)
            # update rear pointer to point to a new node
            self.rear = new_node

    # removing from beginning (First Out)
    def remove_from_head(self):
        # if list empty return Null
        if self.head == None and self.rear == None:
            return None
        # check if there is only one node in the list
        if self.head == self.rear:
            # store the info of the node that is going to be removed
            info = self.head.info
            # remove the node and set both pointers to null
            self.head = None
            self.rear = None
            return info
        # otherwise assign head pointer to next node and remove node
        else:
            # store the removing info of the node
            info = self.head.info
            # set head pointer to next node
            self.head = self.head.next_node
            return info
        
