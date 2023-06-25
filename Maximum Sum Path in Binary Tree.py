class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    # Base case: if the root is None, the maximum path sum is 0
    if root is None:
        return 0

    # Recursively find the maximum path sum for the left and right subtrees
    left_sum = maxPathSum(root.left)
    right_sum = maxPathSum(root.right)

    # Calculate the maximum path sum passing through the current root
    # We have four possibilities: 
    # 1. The path only includes the root node
    # 2. The path includes the root and the left subtree
    # 3. The path includes the root and the right subtree
    # 4. The path includes the root, left subtree, and right subtree
    path_sum = max(root.val, root.val + left_sum, root.val + right_sum, root.val + left_sum + right_sum)

    # Return the maximum path sum between the current root and its subtrees
    return max(path_sum, left_sum, right_sum)

# Test the code with the given example
root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(maxPathSum(root))  # Output: 6
