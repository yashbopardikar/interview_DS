"""LinkedIn Question:Tree has keys and values, values represent sum of this and child node values

NOTE: This is not a binary tree
When merging - absent branches should be created, and values for existing branches are summed
Keys are unique among child nodes of a single parent
Merging is only done of keys that have the same path of keys to the root. E.g. in example given if source has 'M' node under 'C' it doesn't get merged with the 'M' under 'W'.
Child nodes could be stored in any order

  Source:            Target:                      Result:
  ROOT:22             ROOT:20                       ROOT:42

W:2 K:16 C:4        W:5 K:2 R:13             W:7  K:18    C:4 R:13

V:3 E:6  F:7        M:5 M:2  P:13         M:5 V:3 E:6 F:7 M:2 P:13

"""

class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = {}

    def add_child(self, node):
        self.children[node.key] = node

    def __repr__(self, level=0):
        """Helper to visualize the tree structure"""
        ret = "\t" * level + f"{self.key}:{self.value}\n"
        for child in self.children.values():
            ret += child.__repr__(level + 1)
        return ret

class Solution:

    def merge_trees(self, source, target):
        if not source:
            return target
        if not target:
            return source

        target.value += source.value

        for key, source_child in source.children.items():
            if key in target.children:
                self.merge_trees(source_child, target.children[key])
            else:
                target.children[key] = source_child

        return target

source_root = TreeNode("ROOT", 22)
source_root.add_child(TreeNode("W", 2))
source_root.add_child(TreeNode("C", 4))

k_src = TreeNode("K", 16)
k_src.add_child(TreeNode("V", 3))
k_src.add_child(TreeNode("E", 6))
k_src.add_child(TreeNode("F", 7))
source_root.add_child(k_src)

# Target Tree
target_root = TreeNode("ROOT", 20)
target_root.add_child(TreeNode("R", 13))

w_tgt = TreeNode("W", 5)
w_tgt.add_child(TreeNode("M", 5))
target_root.add_child(w_tgt)

k_tgt = TreeNode("K", 2)
k_tgt.add_child(TreeNode("M", 2))
k_tgt.add_child(TreeNode("P", 13))
target_root.add_child(k_tgt)

# Perform Merge
sol = Solution()
merged_tree = sol.merge_trees(source_root, target_root)

print("Resulting Merged Tree:")
print(merged_tree)


