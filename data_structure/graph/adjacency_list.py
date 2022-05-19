# add_node

def add_node(v):
    if v in graph:
        print(v, "is already present in the graph.")
    else:
        graph[v] = []

# add_edge

def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        graph[v2].append(v1)
        graph[v1].append(v2)

graph = {}
add_node('A')
add_node('B')
add_node('C')
add_edge("A","B")
print(graph)