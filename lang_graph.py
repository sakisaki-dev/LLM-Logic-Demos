from langgraph.graph import StateGraph, END

# ============================================================
#                KNOWLEDGE BASE (FACTS + RULES)
# ============================================================

facts = [
    "parent(john, mary)",
    "parent(mary, susan)",
    "parent(susan, lisa)",
    "parent(john, alex)",
    "parent(alex, kevin)",
    "parent(sarah, tom)",
    "male(john)",
    "male(alex)",
    "male(kevin)",
    "female(mary)",
    "female(susan)",
    "female(lisa)"
]


def extract_pairs(key, fact_list):
    """Extract (a,b) from key(a,b)."""
    result = []
    for f in fact_list:
        if f.startswith(key):
            inside = f[f.index("(")+1:f.index(")")]
            a, b = inside.split(",")
            result.append((a.strip(), b.strip()))
    return result


def grandparent(x, y):
    """grandparent(X,Y) :- parent(X,Z), parent(Z,Y)."""
    parents = extract_pairs("parent", facts)

    # children of X
    children_of_x = [child for (p, child) in parents if p == x]

    # if any child is a parent of Y
    for c in children_of_x:
        if (c, y) in parents:
            return True

    return False


def ancestor(x, y):
    """Recursive ancestor(X,Y)."""
    parents = extract_pairs("parent", facts)

    if (x, y) in parents:
        return True

    for (p, child) in parents:
        if p == x and ancestor(child, y):
            return True

    return False


# ============================================================
#                       LANGGRAPH
# ============================================================

class State(dict):
    question: str
    retrieved: list
    relevant: bool
    refined: str
    answer: str


# ============================================================
#                           NODES
# ============================================================

def retrieve(state: State):
    q = state["question"].lower()
    retrieved = [f for f in facts if any(w in f.lower() for w in q.split())]
    state["retrieved"] = retrieved
    return state


def judge(state: State):
    state["relevant"] = len(state["retrieved"]) > 0
    return state


def refine(state: State):
    q = state["question"].lower()

    if "grandparent" in q:
        target = q.split("of")[-1].strip().replace("?", "")
        parents = extract_pairs("parent", facts)

        individuals = {a for (a, b) in parents}

        gps = [x for x in individuals if grandparent(x, target)]

        if gps:
            state["refined"] = f"Grandparent(s) of {target}: {', '.join(gps)}"
        else:
            state["refined"] = f"No grandparents found for {target}."

        return state

    if "ancestor" in q:
        target = q.split("of")[-1].strip().replace("?", "")
        parents = extract_pairs("parent", facts)
        individuals = {a for (a, b) in parents} | {b for (a, b) in parents}

        results = [x for x in individuals if ancestor(x, target)]

        state["refined"] = f"Ancestors of {target}: {', '.join(results)}"
        return state

    state["refined"] = (
        "Cannot answer question using rules.\n"
        "Retrieved facts:\n" + "\n".join(state["retrieved"])
    )
    return state


def answer(state: State):
    state["answer"] = state["refined"]
    return state


# ============================================================
#                         BUILD GRAPH
# ============================================================

workflow = StateGraph(State)

workflow.add_node("retrieve", retrieve)
workflow.add_node("judge", judge)
workflow.add_node("refine", refine)
workflow.add_node("answer", answer)

workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "judge")
workflow.add_edge("judge", "refine")
workflow.add_edge("refine", "answer")
workflow.add_edge("answer", END)

graph = workflow.compile()


# ============================================================
#                            RUN
# ============================================================

if __name__ == "__main__":
    question = "Who is the grandparent of lisa?"
    result = graph.invoke({"question": question})
    print("\n=== FINAL ANSWER ===")
    print(result["answer"])
