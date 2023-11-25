graph = { "a" : ["b"],
"b":["c"],
"c" : ["d", "e"],
"d" :["c","e","f","g"],
"e" : ["c", "d","f"],
"f" : ["e","d"],
"g":["d"],
}
def graph_connected (graph, seen_node=None, start=None):
  if seen_node==None:
    seen_node=set()
    nodes=list(graph.keys()) #list of all the graph keys
    if not start: #start is not given
      start=nodes[0] #vertex at the 0th index will be start
      seen_node.add(start)
      if len(seen_node) <len(nodes):
        for othernodes in graph [start]: # for the adjacent nodes of start
          if othernodes not in seen_node:
            #if adjacent nodes are not present in seen_node
            #it will recursively call itself
            if graph_connected (graph, seen_node, othernodes):
              return True
      else:
        return False
        return True
conn=graph_connected (graph, seen_node=None, start=None)
if conn:
  print("The graph is connected")
else:
  print("The graph is not connected")
