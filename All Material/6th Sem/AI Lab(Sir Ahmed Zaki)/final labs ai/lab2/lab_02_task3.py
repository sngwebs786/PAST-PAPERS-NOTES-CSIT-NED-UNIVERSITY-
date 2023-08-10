#Task 3-1


graph = {
"a": ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
""" returns a list of isolated nodes. """

#Finding Isolated nodes

def find_isolated_nodes (graph):
  isolated = []
  for node in graph: #traverse each node
    if not graph[node]: #value for this node is nothing
      isolated += node # add the node to list
  return isolated

print("Isolated nodes", find_isolated_nodes (graph))

#Task 3-2

graph = {
"a": ["b","d"],
"b" : ["a","c", "d"],
"c" : ["b"],
"d" : ["a","b"],
"e" : [],
}
""" returns a list of isolated nodes. """

#Finding Isolated nodes

def find_isolated_nodes (graph):
  isolated = []
  for node in graph: #traverse each node
    if not graph[node]: #value for this node is nothing
      isolated += node # add the node to list
  return isolated

print("Isolated nodes", find_isolated_nodes (graph))