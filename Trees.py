class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    ans = []
    def postorder(self, rootnode):
        if not rootnode:
            return
        self.postorder(rootnode.left)
        self.postorder(rootnode.right)
        self.ans.append(rootnode.val)

root = TreeNode(5)
root2 = TreeNode(2)
root3 = TreeNode(6)
root.left = root2
root.right = root3

root4 = TreeNode(4)
root5 = TreeNode(1)
root2.left = root5
root2.right = root4

root6 = TreeNode(3)
root7 = TreeNode(9)
root3.left = root6
root3.right = root7

sol = Solution()
sol.postorder(root)
print(sol.ans)

