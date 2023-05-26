from binary_tree import *

set1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, -999]
set2 = [3, 1, 5, 17, 14, 62, -999]
set3 = [17, 12, 75, 12, 37, 60, 90, 11, 15, 35, 45, 53, 67, 97, 95, -999]
set4 = [150, 40, 60, 39, 34, 27, 10, 82, 15, -999]
set5 = [43, 6, 9, -999]
set6 = [14, 15, 13, 17, 18, 12, 16, 94, 46, 34, 74, -999]

# 1. create binary trees
tree1 = Node()
tree2 = Node()
tree3 = Node()
tree4 = Node()
tree5 = Node()
tree6 = Node()

# add values from lists to trees
tree1.make_tree(set1)
tree2.make_tree(set2)
tree3.make_tree(set3)
tree4.make_tree(set4)
tree5.make_tree(set5)
tree6.make_tree(set6)

forest = [tree1, tree2, tree3, tree4, tree5, tree6]

i = 1

print ("All trees:")
for tree in forest:
    print(f"Tree {i}")
    print("Inorder: ")
    tree.inorder_traversal(tree)
    print("\n")
    print("Preorder: ")
    tree.preorder_traversal(tree)
    print("\n")
    print("Postorder: ")
    tree.postorder_traversal(tree)
    print("\n")
    print("Number of Nodes: ")
    print(tree.count(tree))

    print("Number of even nodes: ")
    print(tree.count_even_odd(tree)[0])

    print("Number of odd nodes: ")
    print(tree.count_even_odd(tree)[1])
    print("---------------")
    i = i+1

# combide sets without -999 in first 2 sets
set123 = set1[:-1] + set2[:-1] + set3
set456 = set4[:-1] + set5[:-1] + set6


tree123 = Node()
tree456 = Node()

tree123.make_tree(set123)
tree456.make_tree(set456)

combos = [tree123, tree456]

k = 123

print ("combination trees:")
for combo_tree in combos:
    print(f"Tree{k}")
    print("Inorder: ")
    combo_tree.inorder_traversal(combo_tree)
    print("\n")
    print("Preorder: ")
    combo_tree.preorder_traversal(combo_tree)
    print("\n")
    print("Postorder: ")
    combo_tree.postorder_traversal(combo_tree)
    print("\n")
    print("Number of Nodes: ")
    print(combo_tree.count(combo_tree))

    print("Number of even nodes: ")
    print(combo_tree.count_even_odd(combo_tree)[0])

    print("Number of odd nodes: ")
    print(combo_tree.count_even_odd(combo_tree)[1])
    print("---------------")
    k = 456