from collections import defaultdict

class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for char in word:
            # if char not in root, set it in root as a new dict
            current = current.setdefault(char, {})
        current.setdefault("*")
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if char not in current:
                return False
            current = current[char]
        # if it hits the end, then it's clear
        return "*" in current
            
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current:
                return False
            current = current[char]
        return True

def auto_complete(words, query):
    t = Trie()
    for word in words:
        t.insert(word)

