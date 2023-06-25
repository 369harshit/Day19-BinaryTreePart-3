class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, preorder):
    if not inorder or not preorder:
        return None

    # Create the root node using the first element of the preorder traversal
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root value in the inorder traversal
    root_index = inorder.index(root_val)

    # Recursively build the left and right subtrees
    # The left subtree elements are before the root index in both inorder and preorder traversals
    # The right subtree elements are after the root index in both inorder and preorder traversals
    root.left = buildTree(inorder[:root_index], preorder[1:root_index + 1])
    root.right = buildTree(inorder[root_index + 1:], preorder[root_index + 1:])

    return root

# Test the code with an example
inorder = [40, 20, 50, 10, 60, 30]
preorder = [10, 20, 40, 50, 30, 60]
root = buildTree(inorder, preorder)

# Verify the constructed tree
# Expected output:
#    3
#   / \
#  9  20
#    /  \
#   15   7
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
