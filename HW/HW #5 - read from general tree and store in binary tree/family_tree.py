class BinaryTree:
    def __init__(self, name=None):
        self.name = name
        self.left = None
        self.right = None
        self.parent = None
    
    def preorder_traversal(self, root):
        if not root:
            return
        print(root.name, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print(root.name, end=" ")
        self.inorder_traversal(root.right)
    
    def postorder_traversal(self, root):
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.name, end=" ")
            
    # print tree levels
    def print_tree(self, root):
        if not root:
            return

        queue = [root]
        level = 0

        while queue:
            size = len(queue)
            print("Level", level, ": ", end="")
            for i in range(size):
                curr = queue.pop(0)
                print(curr.name, end=" ")
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            print()
            level += 1

    def find_node(self, root, name):
        if not root:
            return None
        
        if root.name == name:
            return root
        
        left_result = self.find_node(root.left, name)
        if left_result:
            return left_result
        
        right_result = self.find_node(root.right, name)
        if right_result:
            return right_result
        
        return None

    def find_parent(self, root, p):
        node = self.find_node(root, p)
        if node and node.parent:
            return node.parent.name
        else:
            return None

        
    def find_all_children(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.left:
            return []
        
        children = []
        current = node.left
        while current:
            children.append(current.name)
            current = current.right
            
        return children
    
    def find_all_siblings(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.parent:
            return []
        
        siblings = []
        current = node.parent.left
        while current:
            if current.name != p:
                siblings.append(current.name)
            current = current.right
            
        return siblings
    
    def find_oldest_sibling(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.parent:
            return None
        
        oldest = node.parent.left
            
        return oldest.name
    
    def find_youngest_sibling(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.parent:
            return None
        if not node.right:
            return node.name
        
        current = node.right
        youngest_brother = None
        while current:
            if current.name != p:
                youngest_brother = current.name
            current = current.right
            
        return youngest_brother
    
    def find_oldest_child(self,root, p):
        node = self.find_node(root, p)
        if not node or not node.left:
            return None
        
        return node.left.name
    
    def find_youngest_child(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.left:
            return None
        
        current = node.left
        while current.right:
            current = current.right
            
        return current.name

    def find_all_uncles(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.parent or not node.parent.parent:
            return []
        
        uncles = []
        current = node.parent.parent.left
        while current:
            if current.name != node.parent.name:
                uncles.append(current.name)
            current = current.right
            
        return uncles
    
    def find_grandfather(self, root, p):
        node = self.find_node(root, p)
        if not node or not node.parent or not node.parent.parent:
            return None
        
        return node.parent.parent.name

class GeneralTree:
    def __init__(self, name=None):
        self.name = name
        self.children = []
        self.children_no = len(self.children)

    def add_child(self, child_node):
        self.children.append(child_node)

    def create_general_tree(self, data):
        node_dict = {}
        for item in data:
            node_name = item["name"]
            node = node_dict.get(node_name)
            if not node:
                node = GeneralTree(node_name)
                node_dict[node_name] = node

            if "children" in item:
                for child_name in item["children"].values():
                    child_node = node_dict.get(child_name)
                    if not child_node:
                        child_node = GeneralTree(child_name)
                        node_dict[child_name] = child_node
                    node.add_child(child_node)
                    
            if not self.name:
                self.name = node
        return self.name

    def print_tree(self, node=None, level=0):
        if not node:
            node = self.name
        print("  " * level + "- " + node.name)
        for child in node.children:
            self.print_tree(child, level+1)

    # first version converts to binary in a different way
    # def to_binary_tree(self, node=None):

    #     if not node:
    #         node = self.name
        
    #     root = BinaryTree(node.name)

    #     if len(node.children) == 0:
    #         return root
 
    #     if len(node.children) == 1:
    #         root.left = self.to_binary_tree(node.children[0])
    #         root.left.parent = root
    #         return root
        
    #     root.left = self.to_binary_tree(node.children[0])
    #     root.left.parent = root
    #     root.right = self.to_binary_tree(node.children[1])
    #     root.right.parent = root


    #     for child in node.children[2:]:
    #         rightTreeRoot = root.right
    #         while rightTreeRoot.left != None:
    #             rightTreeRoot = rightTreeRoot.left
    #         rightTreeRoot.left = self.to_binary_tree(child)
    #         rightTreeRoot.left.parent = root
        
    #     return root
    
    # convert general tree to binary tree, where the oldest son is left node of parent
    #  and other siblings are the right nodes of the oldest son node and of each other
    def to_binary_2(self, node= None):
        if not node:
            node = self.name
        
        # create a binary tree node with the data of the current node
        root = BinaryTree(node.name)
 
        # convert the first child to a binary tree and set as left child of binary_node
        if node.children:
            root.left = self.to_binary_2(node.children[0])
            root.left.parent = root
        # convert the next sibling to a binary tree and set as right child of binary_node
        current = root.left
        for child in node.children[1:]:
            current.right = self.to_binary_2(child)
            current.right.parent = root
            current = current.right
    
        return root
