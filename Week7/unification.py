# Unifier that allows you to declare which names are variables.
# Works for the example: p(b,X,f(g(Z)))  and  p(z,f(Y),f(Y))

import re
from collections import deque

# === Configuration: list the names you want treated as variables ===
VARIABLES = {"X", "Y", "Z", "z"}    # add or remove names as needed

# === Tokenizer & Parser ===
TOKEN_REGEX = r"\s*([A-Za-z0-9_]+|[,()])\s*"

def tokenize(s):
    return [t for t in re.findall(TOKEN_REGEX, s) if t.strip()]

class Term:
    def __init__(self, name, args=None):
        self.name = name
        self.args = args or []
    def is_variable(self):
        return (not self.args) and (self.name in VARIABLES)
    def is_constant(self):
        return (not self.args) and (self.name not in VARIABLES)
    def __repr__(self):
        if self.args:
            return f"{self.name}({', '.join(map(repr, self.args))})"
        return self.name

def parse_term(tokens):
    name = tokens.popleft()
    if tokens and tokens[0] == '(':
        tokens.popleft()
        args = []
        if tokens[0] != ')':
            while True:
                args.append(parse_term(tokens))
                if tokens[0] == ',':
                    tokens.popleft()
                    continue
                elif tokens[0] == ')':
                    break
        tokens.popleft()
        return Term(name, args)
    return Term(name, [])

def parse(s):
    tks = deque(tokenize(s))
    term = parse_term(tks)
    if tks:
        raise ValueError("Extra tokens after parse: " + " ".join(tks))
    return term

# === Substitution utilities ===
def apply_subst(t, subst):
    if t.is_variable():
        if t.name in subst:
            return apply_subst(subst[t.name], subst)
        return t
    if t.args:
        return Term(t.name, [apply_subst(a, subst) for a in t.args])
    return t

def occurs_check(var, term, subst):
    t = apply_subst(term, subst)
    if t.is_variable():
        return t.name == var
    if t.args:
        return any(occurs_check(var, a, subst) for a in t.args)
    return False

# === Robinson Unification (iterative) ===
def unify(a, b):
    subst = {}
    eqs = deque([(a, b)])
    trace = []
    step = 0
    while eqs:
        step += 1
        s, t = eqs.popleft()
        s = apply_subst(s, subst)
        t = apply_subst(t, subst)
        trace.append((step, s, t, dict(subst)))
        if repr(s) == repr(t):
            continue
        if s.is_variable():
            if occurs_check(s.name, t, subst):
                return None, trace
            subst[s.name] = t
            continue
        if t.is_variable():
            if occurs_check(t.name, s, subst):
                return None, trace
            subst[t.name] = s
            continue
        # both are function/constant (non-variable)
        if s.args and t.args:
            if s.name != t.name or len(s.args) != len(t.args):
                return None, trace
            for sa, ta in reversed(list(zip(s.args, t.args))):
                eqs.appendleft((sa, ta))
            continue
        # different constants -> fail
        return None, trace
    return subst, trace

# === Pretty print trace and result ===
def print_result(subst, trace):
    for item in trace:
        step, s, t, st = item
        print(f"Step {step}: unify {s}  with  {t}    S = {st}")
    if subst is None:
        print("\nResult: UNIFICATION FAILED")
    else:
        # simplify RHS by applying subst
        final = {k: apply_subst(v, subst) for k, v in subst.items()}
        print("\nFinal MGU:")
        for k, v in final.items():
            print(f" {k} -> {v}")

# === Example run ===
if __name__ == "__main__":
    s1 = "p(b,X,f(g(Z)))"
    s2 = "p(z,f(Y),f(Y))"
    t1 = parse(s1)
    t2 = parse(s2)
    subst, trace = unify(t1, t2)
    print("Input:")
    print(" ", s1)
    print(" ", s2)
    print("\nTrace:")
    print_result(subst, trace)
