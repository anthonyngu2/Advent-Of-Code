from collections import defaultdict
#with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Orbits.txt') as file:
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Test.txt') as file:
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
print(orbit_tree)
counter = 0

def traverse_tree(branch):
    for grand_child in traverse_tree(orbit_tree[child]):
        counter += 1
                    
for parent, child in orbit_tree.items():
    traverse_tree(child)
    
print(counter)
#direct = len(orbit_tree.keys())
#print(indirect)
#print(direct)
