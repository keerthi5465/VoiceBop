import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for word in ["play", "pause", "search", "stop"]:
            self.trie.insert(word)

    def test_search(self):
        self.assertTrue(self.trie.search("play"))
        self.assertFalse(self.trie.search("pla"))

    def test_starts_with(self):
        self.assertIn("play", self.trie.starts_with("pl"))
        self.assertEqual(self.trie.starts_with("x"), [])

    def test_fuzzy_search(self):
        self.assertIn("play", self.trie.fuzzy_search("plai", max_distance=1))

if __name__ == "__main__":
    unittest.main()