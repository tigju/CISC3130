from family_tree import GeneralTree

my_family = [
    {"name": "Yuri", "children_no": 2, "children": {"1": "Nick", "2":"Michael"}},
    {"name": "Nick", "children_no": 3, "children": {"1": "Sergio", "2": "Julia", "3": "Vitaliy"}},
    {"name": "Michael", "children_no": 1, "children": {"1": "Lera"}},
    {"name": "Sergio", "children_no": 1, "children": {"1": "Kira"}},
    {"name": "Vitaliy", "children_no": 1, "children": {"1":"Spartak"}}
]
# family tree
#                  Yuri
#                /      \
#           Nick         Michael
#         /  |   \          /
#  Sergio  Julia Vitaliy   Lera
#   /             /
#Kira          Spartak

# example from HW
family_2 = [
    {"name": "Jones", "children_no": 3, "children": {"1": "Bob", "2":"Dan", "3": "Brian"}},
    {"name": "Bob", "children_no": 2, "children": {"1": "Richard", "2": "Jake"}},
    {"name": "Brian", "children_no": 1, "children": {"1": "Michael"}},
    {"name": "Jake", "children_no": 1, "children": {"1": "Bill"}},
    {"name": "Michael", "children_no": 1, "children": {"1": "Deville"}}
]
# tree 2 structure
#                      Jones
#                  /    |     \
#               Bob    Dan     Brian
#              /   \          /
#         Richard   Jake    Michael
#                  /       / 
#               Bill    Deville

# family 3 example
family_3 = [
    {"name": "Kate", "children_no": 3, "children": {"1": "Bob", "2":"Many", "3": "Ocean"}},
    {"name": "Bob", "children_no": 3, "children": {"1": "Jonathan", "2": "Ann", "3": "Miguel"}},
    {"name": "Ann", "children_no": 2, "children": {"1": "Michael", "2": "Oliver"}},
    {"name": "Miguel", "children_no": 2, "children": {"1": "Katalyna", "2": "Yuri"}},
    {"name": "Michael", "children_no": 1, "children": {"1": "Sara"}},
    {"name": "Oliver", "children_no": 2, "children": {"1": "Gigi", "2": "Robert"}},
    {"name": "Yuri", "children_no": 1, "children": {"1": "Susan"}},
    {"name": "Susan", "children_no": 2, "children": {"1": "Lisa", "2": "Ney"}}
]

# Family structure
#                                                Kate
#                               /                         \           \
#                          Bob                               Many      Ocean
#                /          |            \
#           Jonathan      Ann            Miguel
#                       /    \          /       \
#               Michael     Oliver  Katalyna     Yuri
#              /            /   \                /
#          Sara         Gigi  Robert           Susan
#                                             /     \
#                                            Lisa   Ney




# create general tree from my family
print("My Family Tree")
print("===================================")
general_tree = GeneralTree()
general_tree.create_general_tree(my_family)

# print general tree structure
print("General tree:\n")
general_tree.print_tree()
# convert to binary
btree = general_tree.to_binary_2()
# after parsing to binary tree, it looks like this:
#                  Yuri
#                /      
#           Nick         
#         /      \     
#  Sergio          Michael
#   /   \          /
#Kira   Julia     Lera
#          \
#        Vitaliy
#         /
#    Spartak

# print the tree levels
print("\n Converted to Binary tree (levels breadth first):\n")
btree.print_tree(btree)

print("My father")
julia_dad = btree.find_parent(btree, "Julia")
print(julia_dad)

print("My niece's father (my older brother)")
Kira_dad = btree.find_parent(btree, "Kira")
print(Kira_dad)

print("My grandfather's sons (my father and uncle)")
grandfather_sons = btree.find_all_children(btree, "Yuri")
print(grandfather_sons)

print("My father's children (my siblings including me)")
father_kids = btree.find_all_children(btree, "Nick")
print(father_kids)

print("My siblings")
my_siblings = btree.find_all_siblings(btree, "Julia")
print(my_siblings)

print("My father's sibling (my uncle)")
my_dads_sibling = btree.find_all_siblings(btree, "Nick")
print(my_dads_sibling)

print("My uncle's oldest sibling (my father)")
my_uncles_oldest_sibling = btree.find_oldest_sibling(btree, "Michael")
print(my_uncles_oldest_sibling)

print("My youngest sibling")
my_youngest_brother = btree.find_youngest_sibling(btree, "Julia")
print(my_youngest_brother)

print("My father's youngest child (my youngest sibling)")
my_dad_youngest_child = btree.find_youngest_child(btree, "Nick")
print(my_dad_youngest_child)

my_dad_oldest_child = btree.find_oldest_child(btree, "Nick")
print(my_dad_oldest_child)

my_nephews_uncles = btree.find_all_uncles(btree, "Spartak")
print(my_nephews_uncles)

my_uncles = btree.find_all_uncles(btree, "Julia")
print(my_uncles)

my_uncles_uncles = btree.find_all_uncles(btree, "Michael")
print(my_uncles_uncles)

my_grandfather = btree.find_grandfather(btree, "Julia")
print(my_grandfather)

my_niece_grandfather = btree.find_grandfather(btree, "Kira")
print(my_niece_grandfather)




print("\nFamily 2")
print("==================================")
general_t = GeneralTree()
general_t.create_general_tree(family_2)
print("General tree:\n")
general_t.print_tree()
# convert to binary
btree2 = general_t.to_binary_2()
# print the tree levels
print("\n Converted to Binary tree (levels breadth first):\n")
btree2.print_tree(btree2)

print("1)	Who is the father of Brian")
brian_dad = btree2.find_parent(btree2, "Brian")
print(brian_dad)

print("2)	Who are all the sons of Bob?")
bob_sons = btree2.find_all_children(btree2, "Bob")
print(bob_sons)

print("3)	Who are all the brothers of Jake?")
jakes_brothers = btree2.find_all_siblings(btree2, "Jake")
print(jakes_brothers)

print("4)	Who is the oldest brother of Dan?")
dan_oldest_bro = btree2.find_oldest_sibling(btree2, "Dan")
print(dan_oldest_bro)

print("5)	Who is the youngest brother of Dan?")
dan_youngest_bro = btree2.find_youngest_sibling(btree2, "Dan")
print(dan_youngest_bro)

print("6)	Who is the oldest son of Brian?")
brian_oldest_son = btree2.find_oldest_child(btree2, "Brian")
print(brian_oldest_son)

print("7)	Who is the youngest son of Jones?")
jones_youngest_son = btree2.find_youngest_child(btree2, "Jones")
print(jones_youngest_son)

print("8)	Who are the uncles of Michael?")
michaels_uncles = btree2.find_all_uncles(btree2, "Michael")
print(michaels_uncles)

print("9)	Who is the grandfather of Bill?")
bills_grandfather = btree2.find_grandfather(btree2, "Bill")
print(bills_grandfather)


print("\nFamily 3")
print("==================================")
general_t3 = GeneralTree()
general_t3.create_general_tree(family_3)
print("General tree:\n")
general_t3.print_tree()
# convert to binary
btree3 = general_t3.to_binary_2()
# print the tree levels
print("\n Converted to Binary tree (levels breadth first):\n")
btree3.print_tree(btree3)

print("1)	Who is the parent of Oliver")
dad = btree3.find_parent(btree3, "Oliver")
print(dad)

print("2)	Who are all the sons of Kate?")
sons = btree3.find_all_children(btree3, "Kate")
print(sons)

print("3)	Who are all the siblings of Jonathan?")
brothers = btree3.find_all_siblings(btree3, "Jonathan")
print(brothers)

print("4)	Who is the oldest sibling of Yuri?")
oldest_bro = btree3.find_oldest_sibling(btree3, "Yuri")
print(oldest_bro)

print("5)	Who is the youngest brother of Many?")
youngest_bro = btree3.find_youngest_sibling(btree3, "Many")
print(youngest_bro)

print("6)	Who is the oldest son of Oliver?")
oldest_son = btree3.find_oldest_child(btree3, "Oliver")
print(oldest_son)

print("7)	Who is the youngest son of Susan?")
youngest_son = btree3.find_youngest_child(btree3, "Susan")
print(youngest_son)

print("8)	Who are the uncles of Robert?")
uncles = btree3.find_all_uncles(btree3, "Robert")
print(uncles)

print("9)	Who is the grandfather of Lisa?")
grandfather = btree3.find_grandfather(btree3, "Lisa")
print(grandfather)

