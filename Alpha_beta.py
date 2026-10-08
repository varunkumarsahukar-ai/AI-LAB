# Alpha Beta Pruning Algorithm Implementation

import math
def alpha_beta_pruning(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    # Base case: Leaf node reached
    if depth == height:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -math.inf
        for i in range(0, 2):
            value = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, height)
            best = max(best, value)
            alpha = max(alpha, best)
            # Beta cut-off
            if beta <= alpha:
                break
        return best 
    else:
        best = math.inf 
        for i in range(0, 2):
            value = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, height)
            best = min(best, value)
            beta = min(beta, best)
            # Alpha cut-off
            if beta <= alpha:
                break
        return best 

# Main program
values = list(map(int, input("Enter 8 leaf node values: ").split()))
if len(values) != 8:
    print("Please enter exactly 8 values.")
else:
    height = 3
    alpha = -math.inf
    beta = math.inf
    result = alpha_beta_pruning(0, 0, True, values, alpha, beta, height)
    print("The optimal value is: ", result)