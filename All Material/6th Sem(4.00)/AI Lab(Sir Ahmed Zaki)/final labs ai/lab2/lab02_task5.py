#Task 5


graph = {
"a": ["c"],
"b": ["c", "e"],
"c": ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
#Finding all paths between two nodes
def find_all_paths (graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths (graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths
print("All Paths between nodes", find_all_paths (graph, 'a', 'b'))

#Task 5


graph = {
"a": ["c"],
"b": ["c", "e"],
"c": ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
#Finding all paths between two nodes
def find_all_paths (graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if start not in graph:
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths (graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths
print("All Paths between nodes", find_all_paths (graph, 'd', 'b'))
