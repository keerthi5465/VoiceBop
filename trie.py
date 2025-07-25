class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word.lower():
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._dfs(node, prefix.lower(), results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, results)

    def fuzzy_search(self, word, max_distance=1):
        results = []
        self._fuzzy_dfs(self.root, word.lower(), "", 0, max_distance, results)
        return results

    def _fuzzy_dfs(self, node, word, path, edits, max_distance, results):
        if edits > max_distance:
            return
        if not word:
            if node.is_end_of_word and edits <= max_distance:
                results.append(path)
            for char, child in node.children.items():
                self._fuzzy_dfs(child, word, path + char, edits + 1, max_distance, results)
            return
        if node.is_end_of_word and len(word) == 0 and edits <= max_distance:
            results.append(path)
        for char, child in node.children.items():
            if char == word[0]:
                self._fuzzy_dfs(child, word[1:], path + char, edits, max_distance, results)
            else:
                # substitution
                self._fuzzy_dfs(child, word[1:], path + char, edits + 1, max_distance, results)
                # insertion
                self._fuzzy_dfs(child, word, path + char, edits + 1, max_distance, results)
        # deletion
        self._fuzzy_dfs(node, word[1:], path, edits + 1, max_distance, results)