def insert_manual():
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.right = Node("F")
    return root

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def traverse_preorder(node):
    if node:
        print(f" {node.name} ", end="-")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node):
    if node:
        traverse_inorder(node.left)
        print(f" {node.name} ", end="-")
        traverse_inorder(node.right)

def traverse_postorder(node):
    if node:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(f" {node.name} ", end="-")

def get_leaf_nodes(node, leaf_nodes=None):
    if leaf_nodes is None:
        leaf_nodes = []
    if node:
        if not node.left and not node.right:
            leaf_nodes.append(node.name)
        get_leaf_nodes(node.left, leaf_nodes)
        get_leaf_nodes(node.right, leaf_nodes)
    return leaf_nodes

print("Preorder: ")
traverse_preorder(insert_manual())
print("\nInorder: ")
traverse_inorder(insert_manual())
print("\nPostorder: ")
traverse_postorder(insert_manual()) 
print("\nLeaf Nodes: ")
print(get_leaf_nodes(insert_manual()))

