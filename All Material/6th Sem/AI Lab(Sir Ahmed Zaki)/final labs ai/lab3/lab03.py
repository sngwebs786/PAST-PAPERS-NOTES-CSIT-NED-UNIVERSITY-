graph_A = {
'A': ['B', 'E'],
'B': ['F'],
'C': ['G'],
'D': ['E', 'H'],
'E': ['A', 'D', 'H'], 'F': ['B','G', 'I', 'J'], 'G': ['C', 'F', 'J'], 'H': ['D', 'E','I'], 'I': ['F', 'H'], 'J': ['F','G']
}

graph_B={
  'A':['B','C','E'],
  'B':['A','D','E'],
  'C':['A','F','G'],
  'D':['B','E'],
  'E':['A','B'],
  'F':['C'],
  'G':['C']
}


# TASK 1


#visits all the nodes of a graph (connected component) using BFS 
def bfs_connected_component (graph, start):
# keep track of all visited nodes
  explored = []
# keep track of nodes to be checked 
  queue=[start]
#keep Looping until there are nodes still to be checked 
  while queue:
#pop shallowest node (first node) from queue
    node= queue.pop(0)
    if node not in explored:
# add node to list of checked nodes 
      explored.append(node) 
      neighbours=graph[node]
# add neighbours of node to queue \

      for neighbour in neighbours:
        queue.append(neighbour)
  return explored
print(bfs_connected_component (graph_A, 'A'))




#TASK 2


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal): #keep track of explored nodes explored = []
# keep track of all the paths to be checked 
  explored=[]
  queue=[[start]]
# return path if start is goal 
  if start == goal:
    return "That was easy! Start = goal"
  #keeps looping until all possible paths have been checked 
  while queue:
#pop the first path from the queue 
    path = queue.pop(0)
# get the last node from the path 
    node = path[-1]
    if node not in explored:
      neighbours = graph[node]
# go through all neighbour nodes, construct a new path and #push it into the queue
      for neighbour in neighbours: 
        new_path = list(path) 
        new_path.append(neighbour) 
        queue.append(new_path)
# return path if neighbour is goal 
      if neighbour == goal: 
        return new_path
#mark node as explored
    explored.append(node)
# in case there's no path between the 2 nodes 
  return "So sorry, but a connecting path doesn't exist :("

print("Shortest path for graph A for A TO H :",bfs_shortest_path(graph_A, 'A', 'H'))
print("Shortest path for graph B for A TO C :",bfs_shortest_path(graph_B, 'A', 'C'))
print("Shortest path for graph A for A TO C :",bfs_shortest_path(graph_A, 'A', 'C'))
graph = {
'A': set(['B', 'E']),
'B': set(['F']),
'C': set(['G']),
'D': set(['E', 'H']),
'E': set(['A', 'D', 'H']), 
'F': set(['B','G', 'I', 'J']), 
'G': set(['C', 'F', 'J']), 
'H': set(['D', 'E','I']), 
'I': set(['F', 'H']), 
'J': set(['F','G'])
}


def all_paths (graph, start, goal): 
  queue=[ (start, [start])]
  while queue:
    (vertex, path)=queue.pop(0)
    for next in graph[vertex] - set(path): 
      if next==goal:
        yield path + [next]
      else:
        queue.append((next, path+[next]))

print(list(all_paths(graph,'G','D')))



# Question 1

graph_1={
'1':set(['2','3','4']),
'2':set(['1','3','4']),
'3':set(['1','2','3']),
'4':set(['1','2','3','5']),
'5':set(['4','6','7','8']),
'6':set(['5','7','8']),
'7':set(['5','6','8']),
'8':set(['5','6','7']),
}

#part a

print("All nodes ",bfs_connected_component (graph_1, '1'))
print('')

#part b

print("All paths b/w 1 & 6 ",list(all_paths(graph_1, '1','6')))
print('')


#part c
print("Shortest path for graph_1 for 1 TO 6 :",bfs_shortest_path(graph_1, '1', '6'))
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


#part a

print("All nodes ",bfs_connected_component (graph_2, 'A'))
print('')

#part b

print("All paths b/w A&G ",list(all_paths(graph_2, 'A','G')))
print('')


#part c
print("Shortest path for graph_1 for A TO G :",bfs_shortest_path(graph_2, 'A', 'G'))
print('')
