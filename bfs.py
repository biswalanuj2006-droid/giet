visited = []
queue = []

def bfs(graph, start_node):
    global visited, queue
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")
        for neighbour in graph.get(current_node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    # A -> B, C
    # B -> D, E
    # C -> F
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS Traversal starting from node 'A':")
    bfs(graph, 'A')
