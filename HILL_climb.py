# Hill Climbing Algorithm Example

def objective_function(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        current_value = objective_function(current)
        left_value = objective_function(left)
        right_value = objective_function(right)

        # Move to the better neighbor
        if left_value > current_value:
            current = left

        elif right_value > current_value:
            current = right

        else:
            # No better neighbor found
            break

    return current, objective_function(current)


start = int(input("Enter Starting Value: "))

best_position, best_value = hill_climbing(start)

print("\nBest Position:", best_position)
print("Maximum Value:", best_value)