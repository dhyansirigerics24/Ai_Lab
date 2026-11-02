import random
import math

N = 8

# Calculate heuristic
def heuristic(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1

    return conflicts


# Simulated Annealing
def simulated_annealing():

    state = [random.randint(0, N - 1) for _ in range(N)]

    temperature = 1000
    cooling_rate = 0.99
    min_temperature = 0.0001

    iteration = 1

    while temperature > min_temperature:

        current_h = heuristic(state)

        # Print current details
        if iteration % 100 == 0:
            print("Iteration:", iteration,
                  "Temperature:", round(temperature, 2),
                  "Heuristic:", current_h)

        if current_h == 0:
            return state

        new_state = state[:]

        col = random.randint(0, N - 1)
        new_row = random.randint(0, N - 1)
        new_state[col] = new_row

        new_h = heuristic(new_state)
        delta = new_h - current_h

        if delta < 0:
            state = new_state
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                state = new_state

        temperature *= cooling_rate
        iteration += 1

    return None


# Display chessboard
def display(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
solution = simulated_annealing()

if solution is not None:
    print("\n8 Queens Solution Found!")
    print("Final State:", [x + 1 for x in solution])
    print("Heuristic Value:", heuristic(solution))
    print("Final Temperature:", round(temperature, 4) if False else "Reached solution")
    print("\nChessboard:")
    display(solution)
else:
    print("\nCan't find the solution!")