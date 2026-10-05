# 8 Puzzle using IDS

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def moves(state):
    result = []
    pos = state.index(0)

    row, col = pos // 3, pos % 3

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)

            new_state[pos], new_state[new_pos] = \
                new_state[new_pos], new_state[pos]

            result.append(tuple(new_state))

    return result


def DLS(state, depth, limit, path):

    if state == goal:
        return path

    if depth == limit:
        return None

    for next_state in moves(state):

        if next_state not in path:
            result = DLS(next_state, depth + 1,
                         limit, path + [next_state])

            if result:
                return result

    return None


def IDS(start):

    for limit in range(20):
        result = DLS(start, 0, limit, [start])

        if result:
            return result

    return None


# Initial state
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = IDS(start)

for state in solution:
    print(state[0:3])
    print(state[3:6])
    print(state[6:9])
    print()
