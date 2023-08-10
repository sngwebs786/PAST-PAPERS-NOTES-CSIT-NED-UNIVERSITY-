#Task 1-1

graph = { "a" : ["c"],
"b":["c", "e"],
"c" : ["a", "b", "d", "e"],
"d" :["c"],
"e" : ["c", "b"],
"f" : []
}
print(graph["a"])
print("The nodes/vertices of graph:",graph.keys())
#Returns List of dictionary keys
print("The edges of the graph for keys{0} are {1}".format(graph.keys(),graph.values()))
#Returns List of dictionary values
for i,j in graph.items():
  print(i,j)


#Task 1-2


graph = { "a" : ["b"],
"b":["c"],
"c" : ["d", "e"],
"d" :["c","e","f","g"],
"e" : ["c", "d","f"],
"f" : ["e","d"],
"g":["d"],
}
print(graph["a"])
print("The nodes/vertices of graph:",graph.keys())
#Returns List of dictionary keys
print("The edges of the graph for keys{0} are {1}".format(graph.keys(),graph.values()))
#Returns List of dictionary values

for i,j in graph.items():
  print(i,j)