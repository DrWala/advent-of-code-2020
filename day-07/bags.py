from collections import defaultdict

def parse_rule(adj_list, line):
    line = line.strip().split(" ")
    parent = " ".join(line[:2])
    children = " ".join(line[4:])[:-1].split(", ")
    
    clean_children = []
    for child in children:
        child_weight = child.split(" ")[0]
        child = " ".join(child.split(" ")[1:3])
        if child != "other bags":
            clean_children.append((child, child_weight))
    
    adj_list[parent] = clean_children

def transpose(adj_list):
    new_list = defaultdict(list)
    for vertex, edges in adj_list.items():
        # Parent bags need to be reachable, even if they don't point outwards to anyone
        if not vertex in new_list:
            new_list[vertex] = []
        
        for edge in edges:
            new_list[edge[0]].append((vertex, edge[1]))
    return new_list

def traverse(adj_list):
    visited = dict.fromkeys(adj_list.keys(), False)
    parent_bag_set = set()
    def dfs(bag):
        visited[bag] = True
        parent_bag_set.add(bag)
        for neighbour in adj_list[bag]:
            if visited[neighbour[0]] == False:
                dfs(neighbour[0])
    dfs("shiny gold")
    # Do not count the shiny gold bag that we start from
    # thanks to theo for hint
    return len(parent_bag_set) - 1

def traverse_two(adj_list):
    def dfs(bag):
        internal_count = 1
        for neighbour in adj_list[bag]:
            # It is a directed graph and we cannot discount the possibility of
            # seeing the same vertices again so we cannot have a visited array
            # if visited[neighbour[0]] == False:
            internal_count += int(neighbour[1]) * dfs(neighbour[0])
        return internal_count
    
    count = dfs("shiny gold") - 1
    # Do not count the shiny gold bag that we start from
    # thanks to theo for hint
    return count

def solve(input):
    adj_list = defaultdict(list)
    for line in input:
        parse_rule(adj_list, line)    
    
    # Reverse the edgees
    trans_adj_list = transpose(adj_list)
    print(f"Number of bags that can contain shiny gold: {traverse(trans_adj_list)}")
    print(f"Number of bags that can contain shiny gold: {traverse_two(adj_list)}")

file = open("input.txt", "r")
solve(file.readlines())
