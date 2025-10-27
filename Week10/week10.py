
class Node:
    def __init__(self, name, children=None, value=None):
        self.name = name
        self.children = children or []
        self.value = value


def alpha_beta(node, depth, alpha, beta, maximizing, path, pruned):
    indent = "│   " * depth  # Indentation for tree structure
    print(f"{indent}├── Visiting {node.name}", end="")

    # Base case: leaf node
    if not node.children:
        print(f" (Leaf, Value = {node.value})")
        return node.value, [node.name]

    print(f" [{'MAX' if maximizing else 'MIN'} Node]")

    if maximizing:
        max_eval = float('-inf')
        best_path = []
        for child in node.children:
            eval, child_path = alpha_beta(child, depth + 1, alpha, beta, False, path, pruned)
            if eval > max_eval:
                max_eval = eval
                best_path = [node.name] + child_path
            alpha = max(alpha, eval)
            if beta <= alpha:
                print(f"{indent}│   Pruned remaining children of {node.name} (alpha={alpha}, beta={beta})")
                pruned.append(child.name + " (and below)")
                break
        print(f"{indent}└── {node.name} returns {max_eval} (MAX)")
        return max_eval, best_path

    else:
        min_eval = float('inf')
        best_path = []
        for child in node.children:
            eval, child_path = alpha_beta(child, depth + 1, alpha, beta, True, path, pruned)
            if eval < min_eval:
                min_eval = eval
                best_path = [node.name] + child_path
            beta = min(beta, eval)
            if beta <= alpha:
                print(f"{indent}│   Pruned remaining children of {node.name} (alpha={alpha}, beta={beta})")
                pruned.append(child.name + " (and below)")
                break
        print(f"{indent}└── {node.name} returns {min_eval} (MIN)")
        return min_eval, best_path


# Constructing the tree
D = Node("D", [Node("L1", value=3), Node("L2", value=5)])
E = Node("E", [Node("L3", value=6), Node("L4", value=9)])
F = Node("F", [Node("L5", value=1), Node("L6", value=2)])
G = Node("G", [Node("L7", value=0), Node("L8", value=-1)])

B = Node("B", [D, E])
C = Node("C", [F, G])
A = Node("A", [B, C])  # Root node (MAX)


# Run Alpha-Beta Search
print("\nAlpha-Beta Pruning Tree Traversal:\n")
pruned = []
value, best_path = alpha_beta(A, 0, float('-inf'), float('inf'), True, [], pruned)

print("\nFINAL RESULT")
print("Optimal Value of Root (A):", value)
print("Best Path from Root to Leaf:", " → ".join(best_path))
print("\nPruned Branches:")
if pruned:
    for p in pruned:
        print(" -", p)
else:
    print(" - None")
print("\n code by Sushanth Rai")
