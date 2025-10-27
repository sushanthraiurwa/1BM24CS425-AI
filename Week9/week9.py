from typing import Callable, Any, List

# Define logical connectives
def AND(p: bool, q: bool) -> bool:
    return p and q

def OR(p: bool, q: bool) -> bool:
    return p or q

def NOT(p: bool) -> bool:
    return not p

def IMPLIES(p: bool, q: bool) -> bool:
    return (not p) or q


# Quantifiers
def FORALL(domain: List[Any], predicate: Callable[[Any], bool]) -> bool:
    """Universal quantifier: True if predicate(x) holds for all x in domain"""
    return all(predicate(x) for x in domain)

def EXISTS(domain: List[Any], predicate: Callable[[Any], bool]) -> bool:
    """Existential quantifier: True if predicate(x) holds for some x in domain"""
    return any(predicate(x) for x in domain)


# Example predicates
def is_even(x: int) -> bool:
    return x % 2 == 0

def is_positive(x: int) -> bool:
    return x > 0


# Example FOL statements
if __name__ == "__main__":
    domain = list(range(-3, 6))  # domain = {-3, -2, -1, 0, 1, 2, 3, 4, 5}

    # ∀x (is_even(x) → is_positive(x))
    statement1 = FORALL(domain, lambda x: IMPLIES(is_even(x), is_positive(x)))

    # ∃x (is_even(x) ∧ ¬is_positive(x))
    statement2 = EXISTS(domain, lambda x: AND(is_even(x), NOT(is_positive(x))))

    print("Domain:", domain)
    print("Statement 1: ∀x (is_even(x) → is_positive(x)) =", statement1)
    print("Statement 2: ∃x (is_even(x) ∧ ¬is_positive(x)) =", statement2)
    print("code by Sushanth Rai")
