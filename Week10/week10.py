
import math

# -----------------------------------------
# BUILD TREE AS A COMPLETE BINARY TREE
# -----------------------------------------
def build_tree(values):
    nodes = values[:]  # leaves only
    return nodes

# -----------------------------------------
# PRETTY PRINT TREE (Dynamic)
# -----------------------------------------
def print_tree(values):
    print("\n====================")
    print("       GAME TREE")
    print("====================\n")

    n = len(values)
    height = math.ceil(math.log2(n + 1))
    index = 0

    # Print levels from root to leaves
    for level in range(height):
        count = 2 ** level
        gap = " " * (2 ** (height - level))
        row = ""

        for i in range(count):
            if index < len(values):
                if level == 0:
                    row += gap + "(MAX)" + gap
                elif level % 2 == 1:
                    row += gap + "(MIN)" + gap
                else:
                    row += gap + "(MAX)" + gap
                index += 1
        print(row)

    # Print leaves
    print("\nLeaf Values:")
    print(values, "\n")

# -----------------------------------------
# ALPHA-BETA (General Binary Tree Logic)
# -----------------------------------------
def alpha_beta(index, isMax, values, alpha, beta):
    # If leaf node
    if index >= len(values):
        return None
    if (index * 2 + 1) >= len(values) and (index * 2 + 2) >= len(values):
        return values[index]

    if isMax:
        best = -999
        left = alpha_beta(index * 2 + 1, False, values, alpha, beta)
        if left is not None:
            best = max(best, left)
            alpha = max(alpha, best)
        if alpha >= beta:
            return best

        right = alpha_beta(index * 2 + 2, False, values, alpha, beta)
        if right is not None:
            best = max(best, right)
            alpha = max(alpha, best)
        return best

    else:
        best = 999
        left = alpha_beta(index * 2 + 1, True, values, alpha, beta)
        if left is not None:
            best = min(best, left)
            beta = min(beta, best)
        if beta <= alpha:
            return best

        right = alpha_beta(index * 2 + 2, True, values, alpha, beta)
        if right is not None:
            best = min(best, right)
            beta = min(beta, best)
        return best

# -----------------------------------------
# MAIN
# -----------------------------------------
values = list(map(int, input("Enter leaf values separated by space: ").split()))

tree = build_tree(values)
print_tree(tree)

result = alpha_beta(0, True, tree, -999, 999)

print("====================")
print(" Alpha-Beta Result")
print("====================")
print("Root Value =", result)
print("====================\n")
print("Code By : Sushanth Rai\n")

