#Task 9

graph = { "a" : ["b"],
"b":["c"],
"c" : ["d", "e"],
"d" :["c","e","f","g"],
"e" : ["c", "d","f"],
"f" : ["e","d"],
"g":["d"],
}
def find_degree (graph, node):
  degree=0
  t=[]
  for neighbour in graph [node ]:
    t.append(neighbour)
    degree=degree+1
  return degree
Degree=find_degree(graph, "c")
print("degree of the vertex:", Degree)
