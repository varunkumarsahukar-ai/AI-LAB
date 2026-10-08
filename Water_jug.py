# Water Jug Problem Solver using BFS

from collections import deque

def water_jug(cap1, cap2, target_state):
    visited = set()
    queue = deque()

    # Queue stores: (jug1_water, jug2_water, path_history)
    queue.append((0, 0, []))

    while queue:
        j1, j2, path = queue.popleft()
        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))
        current_path = path + [(j1, j2)]

        # Check if the target state is reached
        if (j1, j2) == target_state:
            return current_path

        # Generate all possible next states
        next_moves = [
            (cap1, j2),  # Fill jug1
            (j1, cap2),  # Fill jug2
            (0, j2),  # Empty jug1
            (j1, 0),  # Empty jug2
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),  # Pour jug1 -> jug2
            (j1 + min(cap1 - j1, j2), j2 - min(cap1 - j1, j2)),  # Pour jug2 -> jug1
        ]

        for move in next_moves:
            if 0 <= move[0] <= cap1 and 0 <= move[1] <= cap2 and move not in visited:
                queue.append((move[0], move[1], current_path))

    return None

# Solve for Jug1 capacity = 4L, Jug2 capacity = 3L, and target state = (2, 3)
target_state = (2, 3)
solution = water_jug(4, 3, target_state)

if solution:
    print(f"Steps to reach the target state {target_state}:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")