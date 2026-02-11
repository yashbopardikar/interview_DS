
class Trie:
    def __init__(self):
        self.children = {}
        self.enfOfWord = False

    def insert (self, word:str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.endOfWord = True


    def search(self, word:str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endOfWord

    def startsWith(self, prefix:str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))