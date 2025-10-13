# Forward Chaining Example: Prove Robert is a criminal

# Known facts
facts = {
    "American(Robert)",
    "Enemy(A, America)",
    "Missile(T1)",
    "Owns(A, T1)"
}

# Rules
rules = [
    ("Enemy(x, America)", "Hostile(x)"),
    ("Missile(x)", "Weapon(x)"),
    ("Missile(x) ∧ Owns(A, x)", "Sells(Robert, x, A)"),
    ("American(p) ∧ Weapon(q) ∧ Sells(p, q, r) ∧ Hostile(r)", "Criminal(p)")
]

# Function to check and apply rules
def apply_rules(facts):
    new_facts = set()
    
    # Step 1: Enemy(x, America) -> Hostile(x)
    if "Enemy(A, America)" in facts and "Hostile(A)" not in facts:
        print("Step 1: Enemy(A, America) → Hostile(A)")
        new_facts.add("Hostile(A)")
    
    # Step 2: Missile(x) -> Weapon(x)
    if "Missile(T1)" in facts and "Weapon(T1)" not in facts:
        print("Step 2: Missile(T1) → Weapon(T1)")
        new_facts.add("Weapon(T1)")
    
    # Step 3: Missile(x) ∧ Owns(A, x) -> Sells(Robert, x, A)
    if "Missile(T1)" in facts and "Owns(A, T1)" in facts and "Sells(Robert, T1, A)" not in facts:
        print("Step 3: Missile(T1) ∧ Owns(A, T1) → Sells(Robert, T1, A)")
        new_facts.add("Sells(Robert, T1, A)")
    
    # Step 4: American(p) ∧ Weapon(q) ∧ Sells(p, q, r) ∧ Hostile(r) -> Criminal(p)
    if {"American(Robert)", "Weapon(T1)", "Sells(Robert, T1, A)", "Hostile(A)"} <= facts and "Criminal(Robert)" not in facts:
        print("Step 4: American(Robert) ∧ Weapon(T1) ∧ Sells(Robert, T1, A) ∧ Hostile(A) → Criminal(Robert)")
        new_facts.add("Criminal(Robert)")
    
    return new_facts

# Forward Chaining Loop
step = 1
while True:
    new_facts = apply_rules(facts)
    if not new_facts:
        break
    facts |= new_facts
    step += 1

print("\n✅ Final Facts:")
for fact in facts:
    print(fact)
