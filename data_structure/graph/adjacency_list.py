# add_node

def add_node(v):
    if v in graph:
        print(v, "is already present in the graph.")
    else:
        graph[v] = []

# add_edge

def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        list1 = [v1, cost]
        list2 = [v2, cost]
        graph[v2].append(list1)
        graph[v1].append(list2)

graph = {}
add_node('A')
add_node('B')
add_node('C')
add_edge("A", "B", 20)
add_edge("A", "C", 10)
print(graph)