#Task 4


graph = {
"a" : ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"F": []
}
#Finding path between two nodes
def find_path(graph, start, end, path=[]): #empty list to save values of path
  path = path + [start] # adding first node
  if start == end: # check if both are same
    return path
  if start not in graph:
#if start is not present in graph; returns true if key is in dictionary, false otherwise
    return None
#if start and end are not same find the path
  for node in graph[start]: #for particular node 'a' traverse the neighbours
    if node not in path:
      newpath = find_path(graph, node, end, path)
#recursive function; backtrack finds the vertices which are not present in path yet
      if newpath:
        return newpath
  return None

print("Path between nodes", find_path(graph, 'e', 'd'))
#Task 4



graph = {
"a" : ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"F": []
}
#Finding path between two nodes
def find_path(graph, start, end, path=[]): #empty list to save values of path
  path = path + [start] # adding first node
  if start == end: # check if both are same
    return path
  if start not in graph:
#if start is not present in graph; returns true if key is in dictionary, false otherwise
    return None
#if start and end are not same find the path
  for node in graph[start]: #for particular node 'a' traverse the neighbours
    if node not in path:
      newpath = find_path(graph, node, end, path)
#recursive function; backtrack finds the vertices which are not present in path yet
      if newpath:
        return newpath
  return None

print("Path between nodes", find_path(graph, 'd', 'b'))
