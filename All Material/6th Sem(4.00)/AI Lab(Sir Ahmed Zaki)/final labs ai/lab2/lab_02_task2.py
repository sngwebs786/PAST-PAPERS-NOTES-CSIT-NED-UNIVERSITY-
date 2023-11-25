#Task 2-1


graph = {
"a": ["c"],
"b" : ["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" : ["c"],
"e" : ["c", "b"],
"f" : []
}
def generate_edges (graph):
  edges = [] # empty list
  for node in graph: #traversing through graph
    for neighbour in graph [node]: # takes particular node
       edges.append((node, neighbour))
  return edges
print("Generating Edges:", generate_edges (graph)) #using function

#Task 2-2

graph = {
"1": ["2","3"],
"2" : ["1", "3"],
"3" : ["1", "2", "4"],
"4" : ["3"],
}
def generate_edges (graph):
  edges = [] # empty list
  for node in graph: #traversing through graph
    for neighbour in graph [node]: # takes particular node
       edges.append((node, neighbour))
  return edges
print("Generating Edges:", generate_edges (graph)) #using function
