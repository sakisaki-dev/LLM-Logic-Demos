import copy

def is_variable(x):
    return isinstance(x, str) and len(x) > 0 and x[0].isupper()

def occurs_check(var, x, theta):
    if var == x:
        return True
    if is_variable(x) and x in theta:
        return occurs_check(var, theta[x], theta)
    if isinstance(x, list):
        for xi in x:
            if occurs_check(var, xi, theta):
                return True
    return False

def unify(x, y, theta):
    if theta is None:
        return None
    if isinstance(x, str) and is_variable(x) and x in theta:
        return unify(theta[x], y, theta)
    if isinstance(y, str) and is_variable(y) and y in theta:
        return unify(x, theta[y], theta)

    if x == y:
        return theta

    if is_variable(x):
        return unify_var(x, y, theta)
    if is_variable(y):
        return unify_var(y, x, theta)

    if isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        theta1 = theta
        for xi, yi in zip(x, y):
            theta1 = unify(xi, yi, theta1)
            if theta1 is None:
                return None
        return theta1

    return None

def unify_var(var, x, theta):
    # if var is already bound - unify
    if var in theta:
        return unify(theta[var], x, theta)
    # if is var && bound in theta - unify
    if is_variable(x) and x in theta:
        return unify(var, theta[x], theta)

    if occurs_check(var, x, theta):
        return None

    new_theta = theta.copy()
    new_theta[var] = x
    return new_theta

def substitute(expr, theta):
    if isinstance(expr, list):
        return [substitute(e, theta) for e in expr]
    if isinstance(expr, str) and is_variable(expr) and expr in theta:
        return theta[expr]
    return expr

def backward_chain(kb, query, theta=None):
    if theta is None:
        theta = {}

    # try facts
    for fact in kb["facts"]:
        sigma = unify(query, fact, theta)
        if sigma is not None:
            yield sigma

    # try rules
    for (head, body) in kb["rules"]:
        sigma = unify(query, head, theta)
        if sigma is None:
            continue

        new_theta = sigma
        success = True
        for clause in body:
            instantiated = substitute(clause, new_theta)
            results = list(backward_chain(kb, instantiated, new_theta))
            if not results:
                success = False
                break
            new_theta = results[0]

        if success:
            yield new_theta
kb = {
    "facts": [
        ["parent", "alice", "bob"],
        ["parent", "bob", "charlie"],
        ["parent", "charlie", "david"],
        ["male", "bob"],
        ["male", "charlie"],
        ["female", "alice"],
    ],

    "rules": [
        ( ["ancestor", "X", "Y"], [["parent", "X", "Y"]] ),
        ( ["ancestor", "X", "Y"], [["parent", "X", "Z"], ["ancestor", "Z", "Y"]] )
    ]
}

def test_backward_chaining():
    print("\nTest 1: Who are Alice's descendants?")
    query = ["ancestor", "alice", "Y"]
    results = list(backward_chain(kb, query))
    print(results)

    print("\nTest 2: Who are Bob's descendants?")
    query = ["ancestor", "bob", "Y"]
    results = list(backward_chain(kb, query))
    print(results)

    print("\nTest 3: Who is Charlie's parent?")
    query = ["parent", "X", "charlie"]
    results = list(backward_chain(kb, query))
    print(results)

    print("\nTest 4: Check if Alice is female")
    query = ["female", "alice"]
    results = list(backward_chain(kb, query))
    print(results)

if __name__ == "__main__":
    test_backward_chaining()