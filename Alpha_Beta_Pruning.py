
def alpha_beta(node, depth, alpha, beta, maximizing_player, path=None):
    if path is None:
        path = []

    # Base condition
    if depth == 0 or isinstance(node, int):
        return node, path

    if maximizing_player:
        max_eval = float('-inf')
        best_path = []

        for i, child in enumerate(node):
            eval_value, child_path = alpha_beta(
                child, depth - 1, alpha, beta, False,
                path + [i]
            )

            if eval_value > max_eval:
                max_eval = eval_value
                best_path = child_path

            alpha = max(alpha, max_eval)

            # Pruning condition
            if alpha >= beta:
                break

        return max_eval, best_path

    else:
        min_eval = float('inf')
        best_path = []

        for i, child in enumerate(node):
            eval_value, child_path = alpha_beta(
                child, depth - 1, alpha, beta, True,
                path + [i]
            )

            if eval_value < min_eval:
                min_eval = eval_value
                best_path = child_path

            beta = min(beta, min_eval)

            # Pruning condition
            if alpha >= beta:
                break

        return min_eval, best_path


# Game tree
tree = [
    [3, 5],
    [6, 9],
    [1, 2]
]

# Initial call
result, path = alpha_beta(
    tree,
    3,
    float('-inf'),
    float('inf'),
    True
)

# Print result
print("Optimal Value:", result)
print("Optimal Path:", path)

# Print path values
node = tree
print("Path Values:", end=" ")

for index in path:
    node = node[index]
    print(node, end=" ")

print()
