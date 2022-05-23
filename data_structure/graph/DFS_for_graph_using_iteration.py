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

def DFS_iterative(node, graph):
    visited = set()
    if node not in graph:
        print("Node not present in the graph.")
        return
    stack = []
    stack.append(node)
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

    

graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "E")
add_edge("B", "D")
add_edge("C", "D")
add_edge("E", "D")
print(graph)
DFS_iterative("A", graph)