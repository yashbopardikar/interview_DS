class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Codec:
    def serilaize(self,root):
        resp = []
        def dfs(node):
            if not node:
                resp.append('null')
                return
            resp.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(resp)


    def deserialize(self, data):
        self.idx = 0
        if not data:
            return
        values = data.split(",")

        def dfs():
            if values[self.idx] == "null":
                self.idx +=1
                return None
            node = TreeNode(int(values[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

ser = Codec()
deser = Codec()


# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left = TreeNode(5)
ans = deser.deserialize(ser.serilaize(root))
print(ans.val)