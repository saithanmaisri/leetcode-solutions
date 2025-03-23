class TrieNode:
    def __init__(self):
        self.child = {}
        self.ifend = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None: 
        cur = self.root
        for c in word:
            if c not in cur.child: 
                cur.child[c] = TrieNode()
            cur = cur.child[c] 
        cur.ifend = True

    def search(self, word: str) -> bool:
        def dfs(j, root): 
            cur = root
            for i in range(j, len(word)): 
                c = word[i]
                # case 1
                if c == ".":
                    for child in cur.child.values(): 
                        if dfs(i + 1, child):
                            return True 
                    return False
                # case 2 
                else:
                    if c not in cur.child: 
                        return False
                    cur = cur.child[c] 
            return cur.ifend
        return dfs(0, self.root)
