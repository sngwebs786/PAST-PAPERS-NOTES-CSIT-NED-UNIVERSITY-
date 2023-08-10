# TASK-1

graph1={
'A':['B','E','C'],
'B':['D','E'],
'C':[],
'D':[],
'E':[]
}
def dfs(graph, node, visited):
  if node not in visited:
    visited. append (node)
    for n in graph[node]:
        dfs(graph,n, visited)
  return visited
visited = dfs(graph1, 'A', [])
print(visited)


# TASK-2

graph = {
    'A': set(['B', 'E', 'C']),
    'B': set(['D', 'E']),
    'C': set([]),
    'D': set([]),
    'E': set([])
}

def find_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

print(find_path(graph, 'A', 'E'))


# TASK-3

graph = {
    'A': set(['B', 'E', 'C']),
    'B': set(['D', 'E']),
    'C': set([]),
    'D': set([]),
    'E': set([])
}

def find_shortest_path(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

print(find_shortest_path(graph, 'A', 'E'))



def all_paths_dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    visited.add(start)
    path = path + [start]
    if start == goal:
        yield path
    else:
        for next_vertex in graph[start] - visited:
            yield from all_paths_dfs(graph, next_vertex, goal, visited, path)
    visited.remove(start)

graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'C', 'D']),
    'C': set(['A', 'B', 'D']),
    'D': set(['B', 'C', 'E']),
    'E': set(['D', 'F']),
    'F': set(['E', 'G']),
    'G': set(['F', 'H']),
    'H': set(['G', 'I']),
    'I': set(['H', 'J']),
    'J': set(['I', 'K']),
    'K': set(['J'])
}

print(list(all_paths_dfs(graph, 'A', 'D')))





# Question 1

graph = {
'1': set(['2', '4','3']),
'2': set(['1','3','4']),
'3': set(['1','2','4']),
'4': set(['1', '2','3','5']),
'5': set(['4', '6', '7','8']), 
'6': set(['5','7','8']), 
'7': set(['5', '6', '8']),
'8': set(['5', '6', '7']),
}






# Part a
visited_task1 = dfs(graph, '1', [])
print("Traversal path using DFS:", visited_task1)
print('')

# Part b

single_path_task2 = find_path(graph, '1', '6')
print("Single path between 1 & 6:", single_path_task2)
print('')

# Part c
all_paths_task3 = list(all_paths_dfs(graph, '1', '6'))  # Convert generator to list
print("All paths between 1 & 6:", all_paths_task3)
print('')

# Part d
shortest_path_task4 = find_shortest_path(graph, '1', '6')
print("Shortest path between 1 & 6:", shortest_path_task4)
print('')



# Question 2

graph_2 = {
'A': set(['B', 'C','D']),
'B': set(['A','E']),
'C': set(['A','F']),
'D': set(['A', 'E','G']),
'E': set(['B', 'D', 'G']), 
'F': set(['C','G']), 
'G': set(['D', 'E', 'F'])
}

# Part a
visited_task1 = dfs(graph_2, 'A', [])
print("Traversal path using DFS:", visited_task1)
print('')

# Part b
single_path_task2 = find_path(graph_2, 'A', 'G')
print("Single path between A & G:", single_path_task2)
print('')

# Part c
all_paths_task3 = list(all_paths_dfs(graph_2, 'A', 'G'))  # Convert generator to list
print("All paths between A & G:", all_paths_task3)
print('')
# Part d
shortest_path_task4 = find_shortest_path(graph_2, 'A', 'G')
print("Shortest path between A & G:", shortest_path_task4)
print('')