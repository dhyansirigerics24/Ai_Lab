
# Step 1: Define the knowledge base in CNF
# P -> Q becomes (~P OR Q)

clauses = [
    {'~P', 'Q'},
    {'P'}
]

# Step 2: Negate the query Q
query = 'Q'
clauses.append({'~' + query})

# Step 3: Resolution function
def resolve(c1, c2):
    new_clauses = set()

    for literal in c1:
        opposite = literal[1:] if literal.startswith('~') else '~' + literal

        if opposite in c2:
            new_clause = (c1 | c2) - {literal, opposite}
            new_clauses.add(frozenset(new_clause))

    return new_clauses

# Step 4: Apply resolution
def resolution(clauses):
    clauses = set(frozenset(c) for c in clauses)

    while True:
        new = set()

        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                resolvents = resolve(
                    clause_list[i], clause_list[j]
                )

                if frozenset() in resolvents:
                    return True

                new.update(resolvents)

        if new.issubset(clauses):
            return False

        clauses.update(new)

# Step 5: Display result
if resolution(clauses):
    print("Empty clause obtained!")
    print("Query is proved.")
    print("KB entails the query.")
else:
    print("Query cannot be proved.")
