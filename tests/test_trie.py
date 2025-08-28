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

    def test_empty_trie(self):
        empty_trie = Trie()
        self.assertFalse(empty_trie.search("play"))
        self.assertEqual(empty_trie.starts_with("p"), [])

    def test_case_insensitive(self):
        self.assertTrue(self.trie.search("PLAY"))
        self.assertIn("pause", self.trie.starts_with("PA"))

    def test_fuzzy_higher_distance(self):
        self.assertIn("search", self.trie.fuzzy_search("serch", max_distance=2))

if __name__ == "__main__":
    unittest.main()
