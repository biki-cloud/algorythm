from tree.binary_search_tree import BinarySearchTree

root = [10,5,15,3,7,None,18]
low = 7
high = 15
binary_tree = BinarySearchTree()
for i in root:
    if i:
        binary_tree.insert(i)

def inoder(node) -> None:
    if node is not None:
        inoder(node.left)
        print(node.value)
        inoder(node.right)

inoder(binary_tree.root)
