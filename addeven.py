from BinaryTree import BinaryTree, TreeNode

def addEven(tree):
    if tree is None:
        return 0

    sum = tree.element
    if tree.left is not None:
        sum += addEven(tree.left.left) + addEven(tree.left.right)

    if tree.right is not None:
        sum += addEven(tree.right.left) + addEven(tree.right.right)

    return sum

def main():
    numbers = [11, 42, 26, 31, 56, 85, 74, 68, 93]
    # Build a test tree as given in the picture.
    intTree = BinaryTree()
    intTree.insert(11)
    rootNode = intTree.getRoot()
    rootNode.left = intTree.createNewNode(42)
    rootNode.right = intTree.createNewNode(31)
    rootNode.left.right = intTree.createNewNode(26)
    rootNode.right.left = intTree.createNewNode(56)
    rootNode.right.right = intTree.createNewNode(85)
    rootNode.right.left.left = intTree.createNewNode(74)
    rootNode.right.left.right = intTree.createNewNode(68)
    rootNode.right.left.left.right = intTree.createNewNode(93)


    print("\nInorder (sorted): ", end="")
    intTree.postorder()

    print("\nAdd Even:", addEven(rootNode))

main()