# Given an m x n board of characters and a list of strings words, return all words on the board.
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once in a word.
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()
        for w in words:
            root.insert(w)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(r,c,node,word):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or board[r][c] not in node.children:
                return

            node = node.children[board[r][c]]
            word += board[r][c]
            #visited.add((r, c))
            ch  = board[r][c]
            board[r][c] = "#"
            if node.end:
                res.add(word)
                node.end = False  # enchance
            # ------ Enchance ---------
            if not node.children:
                board[r][c] = ch
                return

            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            # visited.remove((r,c))
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r,c,root, "")

        return list(res)


board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
sol = Solution()
print(sol.findWords(board, words))

