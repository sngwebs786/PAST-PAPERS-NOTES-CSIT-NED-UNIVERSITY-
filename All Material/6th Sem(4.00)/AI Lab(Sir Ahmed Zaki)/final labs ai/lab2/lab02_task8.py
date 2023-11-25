#Task 8

graph = {
"a": ["a","c"],
"b" : ["c", "e"],
"c": ["a", "b", "d", "e"],
"d" : ["c"],
"e": ["c", "b"],
"f" : []
}

graph1 = { "a":["c"],
"c":[]
}
def find_cycle_single_node (graph, start):
  for node in graph[start]:
    if node==start:
      return "cycle exist"
  return "cycle does not exist"
print(find_cycle_single_node (graph, "a"))
print(find_cycle_single_node (graph1, "a"))
