from turtle import right
from stack import arrayStack

class TreeNode:
    #BET node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryExpressionTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def clear_tree(self):
        self.root = None

    def buld_from_postfix(self, postfix_expr):

        stack=arrayStack()
        tokens=postfix_expr.split()

        for token in tokens:
                #node for token
                if self._is_number(token):
                    node=TreeNode(token)
                    stack.push(node)
                #node for operator
                elif token in "+-*/":
                    node = TreeNode(token)

                    #pop right child (LIFO)
                    try:
                        node.right=stack.pop()
                    except IndexError:
                        raise ValueError("ERROR! Stack is empty, too few operands)")
                    #pop left
                    try:
                        node.left=stack.pop()
                    except IndexError:
                        raise ValueError("ERROR! Stack is empty, too few operands)")

                    #push new subtree back
                    stack.push(node)
                else:
                    raise ValueError(f"ERROR! Unsupported token: {token}")
        #pop root
        if not stack.is_empty():
            self.root=stack.pop()
            if not stack.is_empty():
                raise ValueError("ERROR! Unused tokens left on stack")
        else:
            raise ValueError("ERROR! Stack is empty")

    def evaluate_tree(self):
        #evals tree, return result
        if self.is_empty():
            raise ValueError("Tree is empty")
        return self._evaluate_recursive(self.root)

    def _evaluate_recursive(self, node):
        #recursive helper for eval
        if node.left is None and node.right is None:
            return float(node.value)

        left_val = self._evaluate_recursive(node.left)
        right_val=self._evaluate_recursive(node.right)

        if node.value=='+': return left_val+right_val
        if node.value=='-': return left_val-right_val
        if node.value=='*': return left_val*right_val
        if node.value=='/':
            if right_val == 0:
                raise ZeroDivisionError("Can't divide by zero!!!!")
            return left_val/right_val
        return 0

    def infix_trav(self):
        #inorder transversal of infix
        if self.is_empty():
            return ""
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        #reconstrux infix, adds parenthesis for output format

        #if leaf, return value
        if node.left is None and node.right is None:
            return node.value

        left_str=self._inorder_recursive(node.left)
        right_str=self._inorder_recursive(node.right)
        return f"({left_str} {node.value} {right_str})"

    def postfix_trav(self):
        #returns postfix using postorder traversal
        if self.is_empty():
            return ""
        return self._postorder_recursive(self.root).strip()

    def _postorder_recursive(self, node):
        #reconstrux postfix in format
        if node is None:
            return ""

        left_str=self._postorder_recursive(node.left)
        right_str=self._postorder_recursive(node.right)
        return f"{left_str}{right_str}{node.value}"

    def _is_number(self, token):
        #token validation, check if valid number
        try:
            float(token)
            return True
        except ValueError:
            return False



