from collections import defaultdict
#with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Orbits.txt') as file:
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Test1.txt') as file:
    Orbits = file.read().splitlines()
    
def build_tuple_list(orbits_list):
    Orbits =[]
    #create list of tuples of each paired orbits
    for orbit_pair in orbits_list:
        Orbits.append(tuple(orbit_pair.split(')')))

    return Orbits
        
orbits_tuple_list = build_tuple_list(Orbits)

def build_tree(orbit_list):
    #implements default value of list 
    tree = defaultdict(list)
    for pair in orbit_list:
        center, orbiter = pair
        tree[center].append(orbiter)
    
    return tree

orbit_tree = build_tree(orbits_tuple_list)

def traverse_tree(tree, branch):
    counter = 1
    child = tree[branch]
    for child in tree[branch]:
        counter += traverse_tree(tree, child)
    return counter 

indirect = 0
for parent, children in list(orbit_tree.items()):
    for child in children:
        indirect += traverse_tree(orbit_tree,child)
    
print(indirect)

