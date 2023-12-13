# The graph of the video.
graph = {
    "A" : ["B", "C"],
    "B" : ["D", "C"],
    "C" : ["B", "E"],
    "E" : ["F"],
    "F" : [],
    "D" : []
}

# The algorithm.
def dfs(graph, node): 
    visited = []
    stack = []
    
    # Adds the starting node to the stack.
    stack.append(node)

    # Runs until the stack is empty.
    while len(stack)>0:
        node = stack.pop()

        # Only add the neighbors of a node to the stack if it hasn't been visited before.
        if (node not in visited):
            visited.append(node)
            for neighboring_node in graph[node]:
                stack.append(neighboring_node)

    # Returns all the reachable nodes.
    return visited

# Runs the algorithm from node A.
print(dfs(graph, "A"))