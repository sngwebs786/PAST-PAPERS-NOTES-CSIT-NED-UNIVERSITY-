#Task 7 - 1



graph = {
"a" : ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
print("Actual graph", graph) #Adding an edge
def add_edge(graph, edge):
  edge=set (edge) # if you don't want duplicates in list than you will use set
  (n1,n2)=tuple(edge) # same as list; can't be changed
  if n1 in graph:
    graph[n1]=n2
#graph[n1].append(n2)
  return graph
print("add an edge:", add_edge(graph,{"a", "g"}))

#Task 7 - 2:


graph = {
"a" : ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
print("Actual graph", graph) #Adding an edge
def add_edge(graph, edge):
  edge=set (edge) # if you don't want duplicates in list than you will use set
  (n1,n2)=tuple(edge) # same as list; can't be changed
  if n1 in graph:
    graph[n1]=n2
#graph[n1].append(n2)
  return graph
print("add an edge:", add_edge(graph,{"d", "c"}))
