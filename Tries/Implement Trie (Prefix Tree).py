class TrieNode(object):
    def __init__(
        self,
        val ,
        children
    ):
        self.val = val
        self.children = children

class Trie(object):

    def __init__(self):
        self.root = TrieNode('', {})
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                new_node = TrieNode(char, {})
                curr.children[char] = new_node
            curr = curr.children[char]
        curr.children['end'] = TrieNode('', {})
            
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False 
        return True if 'end' in curr.children else False 
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix: 
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False 
        return True  
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
