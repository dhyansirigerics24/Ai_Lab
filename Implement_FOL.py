
# Step 1: Occurs check
def occurs(var, term):
    if isinstance(term, str):
        return var == term

    return any(occurs(var, t) for t in term[1])


# Step 2: Apply substitutions
def substitute(term, subst):
    if isinstance(term, str):
        while term in subst:
            term = subst[term]
        return term

    return (term[0], tuple(substitute(t, subst)
                            for t in term[1]))


# Step 3: Unification function
def unify(x, y, subst=None):
    if subst is None:
        subst = {}

    x = substitute(x, subst)
    y = substitute(y, subst)

    # Same expressions
    if x == y:
        return subst

    # Variable substitution
    if isinstance(x, str):
        if occurs(x, y):
            return None
        subst[x] = y
        return subst

    if isinstance(y, str):
        if occurs(y, x):
            return None
        subst[y] = x
        return subst

    # Check predicate names
    if x[0] != y[0]:
        return None

    # Check number of arguments
    if len(x[1]) != len(y[1]):
        return None

    # Unify corresponding arguments
    for a, b in zip(x[1], y[1]):
        subst = unify(a, b, subst)

        if subst is None:
            return None

    return subst


# Step 4: Define two expressions
expr1 = ("Knows", ("John", "x"))
expr2 = ("Knows", ("y", "Mary"))

# Step 5: Perform unification
result = unify(expr1, expr2)

# Step 6: Display result
if result is not None:
    print("Unification Successful!")
    print("Most General Unifier (MGU):")

    for var, value in result.items():
        print(var, "=", value)
else:
    print("Unification Failed!")
