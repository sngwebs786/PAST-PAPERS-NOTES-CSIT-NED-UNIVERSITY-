# Finding shortest path between two nodes
def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:  # traverse through graph and find neighbors
        if node not in path:  # if neighbor node is not in path
            newpath = find_shortest_path(graph, node, end, path)
            # find shortest path between adjacent nodes and return the result
            if newpath:  # if you find a new path
                if not shortest or len(newpath) < len(shortest):
                    # compare the length of the acquired path with the shortest;
                    # if shortest path is found, assign the acquired path to the shortest variable
                    shortest = newpath
    return shortest

# Define the graph as a dictionary for Part 1
graph_part1 = {
    'a': ['b', 'c'],
    'b': ['a', 'd'],
    'c': ['a'],
    'd': ['b']
}

# Task 6 Part 1

print("Shortest Path between nodes:", find_shortest_path(graph_part1, 'a', 'b'))

# Define the graph as a dictionary for Part 2
graph_part2 = {
    'd': ['b', 'e'],
    'b': ['a', 'd'],
    'e': ['d']
}

# Task 6 Part 2

print("Shortest Path between nodes:", find_shortest_path(graph_part2, 'd', 'b'))
