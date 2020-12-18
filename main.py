from tree.binary_search_tree import BinarySearchTree
class Node(object):
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def inoder(node) -> None:
    if node is not None:
        inoder(node.left)
        print(node.value)
        if low <= node.value and high >= node.value:
            sum += node.value
        inoder(node.right)
    print(sum)

root = [10,5,15,3,7,None,18]
low = 7
high = 15
sum = 0
tree = None
for i in root:
    if i:
        tree = insert(tree,i)


inoder(tree)


