class Node:
    def __init__(self, value=None):
        self.info = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left is None:
            self.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right is None:
            self.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = self.right
            self.right = new_node

# will add values from a list to the binary tree in a breadth first order:
#           1
#          / \
#         2   3
#        / \ / \
#       4  5 6  7
    def make_tree(self, lst):
        if not lst:
            return None
        self.info = lst[0]

        # insert values from the list breadth first
        queue = [self]
        i = 1
        
        while i < len(lst):
            
            if lst[i] == -999:
                break
            curr_node = queue.pop(0)
        
            if lst[i] is not None:
                curr_node.insert_left(lst[i])
                queue.append(curr_node.left)

            i += 1

            if i < len(lst) and lst[i] is not None and lst[i] != -999:
                curr_node.insert_right(lst[i])
                queue.append(curr_node.right)

            i += 1
        return self


    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.info, end=" ")
            self.inorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.info, end=" ")
            

    def preorder_traversal(self, node):
        if node:
            print(node.info, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def count(self, node):
        if not node:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    def count_even_odd(self, node):
        even = 0
        odd = 0
        if node:
            if node.info % 2 == 0:
                even += 1
            else:
                odd += 1
            even += self.count_even_odd(node.left)[0] + self.count_even_odd(node.right)[0]
            odd += self.count_even_odd(node.left)[1] + self.count_even_odd(node.right)[1]
        return (even, odd)

