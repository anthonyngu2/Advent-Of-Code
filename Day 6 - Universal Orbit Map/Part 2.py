from collections import defaultdict
with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Orbits.txt') as file:
#with open ('/Users/anthonynguyen/Desktop/Advent-Of-Code-2019/Day 6 - Universal Orbit Map/Test2.txt') as file:
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


def find_all_path(tree, start_node, path=[], total_path=[]):
    path.append(start_node)
    if len(tree[start_node]) == 0:
        total_path.append(str(path))
        path.pop()
    else:
        for child in tree[start_node]:
            find_all_path(tree,child,path,total_path)
        ## removes items from paths list as recursion is finished, so start at child
        path.pop()
    return total_path

root_path = []
total_path = []
paths_from_root = find_all_path(orbit_tree,'COM', root_path,total_path)

lists_of_path = [eval(path) for path in paths_from_root]

def path_finder(paths, endpoint):
    for path in lists_of_path:
      if path[-1] == endpoint:
          return path

path_to_SAN = path_finder(lists_of_path, 'SAN')
path_to_YOU = path_finder(lists_of_path, 'YOU')

path_diffs = [[node for node in path_to_SAN if node not in path_to_YOU], [node for node in path_to_YOU if node not in path_to_SAN]]
nodes_list = [node for sub_path_diff in path_diff for node in sub_path_diff]
orbital_transfers = len(nodes_list) - 2
print(orbital_transfers)
