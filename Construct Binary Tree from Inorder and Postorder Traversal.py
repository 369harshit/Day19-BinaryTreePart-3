class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    # Create the root node using the last element of the postorder traversal
    root_val = postorder[-1]
    root = TreeNode(root_val)

    # Find the index of the root value in the inorder traversal
    root_index = inorder.index(root_val)

    # Recursively build the left and right subtrees
    # The left subtree elements are before the root index in both inorder and postorder traversals
    # The right subtree elements are after the root index in both inorder and postorder traversals
    root.left = buildTree(inorder[:root_index], postorder[:root_index])
    root.right = buildTree(inorder[root_index + 1:], postorder[root_index:-1])

    return root

# Test the code with an example
inorder = [40, 20, 50, 10, 60, 30]
postorder = [40, 50, 20, 60, 30, 10]
root = buildTree(inorder, postorder)

# Verify the constructed tree
# Expected output:
#           10
#          / \
#        20   30
#        / \   /  
#       40 50 60   
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.left.left.val)
print(root.left.right.val)
print(root.right.left.val)
