import unittest
from command_processor import CommandProcessor

class TestCommandProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = CommandProcessor(["play", "pause", "search", "stop"])

    def test_exact_command(self):
        self.assertEqual(self.processor.process("play"), "Playing...")

    def test_autocomplete(self):
        self.assertIn("Did you mean", self.processor.process("pl"))

    def test_fuzzy(self):
        self.assertIn("Did you mean", self.processor.process("plai"))

    def test_unrecognized(self):
        self.assertEqual(self.processor.process("xyz"), "Command not recognized.")

if __name__ == "__main__":
    unittest.main()