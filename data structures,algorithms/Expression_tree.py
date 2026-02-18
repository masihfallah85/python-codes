#Expression_tree

"""
In this script we implement an expression tree using binary tree
"""


from Binary_tree import binary_tree

def build_expression_tree() -> binary_tree:

    """
    Builds a binary tree representing mathematical expression : ((10 - 2) * 3) + 5
    """
   
    tree = binary_tree()
    
    root_pos = tree.add_root('+')
    
    tree.add_right(root_pos, 5)
    
    mult_pos = tree.add_left(root_pos, '*')

    tree.add_right(mult_pos, 3)
    
    sub_pos = tree.add_left(mult_pos, '-')
    
    tree.add_left(sub_pos, 10)
    tree.add_right(sub_pos, 2)

    return tree, root_pos

def evaluate(tree : binary_tree, position : binary_tree.position):

    """
    Recursively evaluates the expression tree
    """

    if tree.is_leaf(position):

        return position.element()
    
    left_val = evaluate(tree, tree.left(position))

    right_val = evaluate(tree, tree.right(position))
    
    operator = position.element()

    if operator == '+': 

        return left_val + right_val
    
    if operator == '-': 

        return left_val - right_val
    
    if operator == '*':

        return left_val * right_val
    
    if operator == '/':

        return left_val / right_val

def tokenize_tree(tree : binary_tree, position : binary_tree.position) -> str:

    """
    Generates a string representation of the equation using recursion.
    """

    if tree.is_leaf(position):

        return str(position.element())
    
    left_str = tokenize_tree(tree, tree.left(position))

    right_str = tokenize_tree(tree, tree.right(position))

    operator = position.element()
    
    return f"({left_str} {operator} {right_str})"


if __name__ == "__main__":

    expr_tree, tree_root = build_expression_tree()
    
    equation_str = tokenize_tree(expr_tree, tree_root)
    
    result = evaluate(expr_tree, tree_root)
    
    print(f"Equation found in tree: {equation_str}")

    print(f"Calculated Result: {result}")
    
    print(f"Python check: ((10 - 2) * 3) + 5 = {((10 - 2) * 3) + 5}")