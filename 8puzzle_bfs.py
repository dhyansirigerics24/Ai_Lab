from collections import deque

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for dr, dc in moves:
            nr, nc = row + dr, col + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                new_zero = nr * 3 + nc

                new_state = list(state)
                new_state[zero], new_state[new_zero] = \
                    new_state[new_zero], new_state[zero]

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    return None


def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# 0 represents the blank space
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

solution = bfs(start, goal)

if solution:
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        print_puzzle(step)
else:
    print("No solution exists.")
