import random

N = 4

# Calculate heuristic value
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate neighboring states
def get_neighbors(state):
    neighbors = []

    for col in range(N):
        for row in range(N):
            if state[col] != row:
                new_state = state.copy()
                new_state[col] = row
                neighbors.append(new_state)

    return neighbors


# Hill Climbing Algorithm
def hill_climbing():
    current = [random.randint(0, N - 1) for _ in range(N)]

    for iteration in range(1, 4):
        current_h = heuristic(current)

        print("\nIteration:", iteration)
        print("Current State:", current)
        print("Heuristic:", current_h)

        if current_h == 0:
            print("Solution Found!")
            return current

        neighbors = get_neighbors(current)
        best = min(neighbors, key=heuristic)

        print("Best Neighbor:", best)
        print("Best Heuristic:", heuristic(best))

        if heuristic(best) >= current_h:
            print("Local Optimum Reached!")
            break

        current = best

    # Check whether solution is found
    if heuristic(current) == 0:
        print("Solution Found!")
        return current
    else:
        return None


# Display chessboard
def display(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()


# Main program
solution = hill_climbing()

if solution is not None:
    print("\nFinal State:")
    display(solution)
    print("Heuristic Value:", heuristic(solution))
else:
    print("\nCan't find the solution!")
    