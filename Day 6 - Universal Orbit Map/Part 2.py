from collections import defaultdict
#with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Orbits.txt') as file:
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Test2.txt') as file:
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


def find_all_path(tree, start_node, path =[]):
    path.append(start_node)
    if len(tree[start_node]) == 0:
        print(path)
        path.pop()
    else:
        for child in tree[start_node]:
            find_all_path(tree,child,path)
        path.pop()



root_path = []
path_from_root = find_all_path(orbit_tree,'COM', root_path)
print(path_from_root)

