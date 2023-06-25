class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror(root):
    if not root:
        return None

    # Recursively mirror the left and right subtrees
    mirror(root.left)
    mirror(root.right)

    # Swap the left and right children of the current node
    root.left, root.right = root.right, root.left

# Test the code with an example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Before mirroring:
#     1
#    / \
#   2   3
#  / \
# 4   5

mirror(root)

# After mirroring:
#     1
#    / \
#   3   2
#        / \
#       5   4

# Verify the mirror image
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)
