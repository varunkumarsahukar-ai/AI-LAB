from collections import deque

# Function to perform Breadth First Search (BFS)
def bfs(graph, start):

    # Step 1: Create an empty list called visited
    visited = []

    # Step 2: Create an empty queue called queue
    queue = deque()

    # Step 3: Put the start node into the queue
    queue.append(start)

    # Step 4: Mark the start node as visited
    visited.append(start)

    # Step 4.1: While the queue is not empty
    while queue:

        # Current node = pop from the queue
        current_node = queue.popleft()

        # Print the current node
        print(current_node, end=" ")

        # For each neighbour connected to current_node
        for neighbour in graph[current_node]:

            # If neighbour is not visited
            if neighbour not in visited:

                # Add neighbour to visited
                visited.append(neighbour)

                # Add neighbour to the back of the queue
                queue.append(neighbour)

    # Step 5: Empty queue is reached
    print("\nQueue is empty. BFS Traversal Completed.")


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting node
start_node = 'A'

# Call the BFS function
print("BFS Traversal:")
bfs(graph, start_node)