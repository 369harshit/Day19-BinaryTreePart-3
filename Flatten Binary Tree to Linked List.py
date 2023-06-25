class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return None

    # Flatten the left and right subtrees recursively
    flatten(root.left)
    flatten(root.right)

    # Store the right subtree temporarily
    temp_right = root.right

    # Connect the flattened left subtree to the root's right
    root.right = root.left
    root.left = None

    # Find the end of the flattened right subtree
    current = root
    while current.right:
        current = current.right

    # Connect the stored right subtree to the end of the flattened right subtree
    current.right = temp_right

# Test the code with an example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)

# Verify the flattened tree
# Expected output:
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#          \
#           5
#            \
#             6
current = root
while current:
    print(current.val)
    current = current.right
