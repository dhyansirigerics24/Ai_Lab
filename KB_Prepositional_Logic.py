
from itertools import product

# Step 1: Define the knowledge base
# P -> Q is equivalent to (not P or Q)
def knowledge_base(P, Q):
    return (not P or Q) and P

# Step 2: Define the query
def query(P, Q):
    return Q

# Step 3: Check entailment using truth table
symbols = ['P', 'Q']
entailed = True

for values in product([False, True], repeat=2):
    P, Q = values

    if knowledge_base(P, Q):
        print("P =", P, "Q =", Q)

        if not query(P, Q):
            entailed = False
            break

# Step 4: Display result
if entailed:
    print("\nKB entails the query")
else:
    print("\nKB does not entail the query")
