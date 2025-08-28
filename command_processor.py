from trie import Trie

class CommandProcessor:
    def __init__(self, commands=None):
        """
        commands: dict of {command_text: response_text}
        """
        self.commands = commands or {}
        self.trie = Trie()
        for cmd in self.commands.keys():
            self.trie.insert(cmd)

    def process(self, command: str) -> str:
        command = command.lower().strip()

        # Exact match
        if self.trie.search(command):
            return self.commands.get(command, f"Executing {command}...")

        # Autocomplete suggestions
        suggestions = self.trie.starts_with(command)
        if suggestions:
            return f"Did you mean: {', '.join(suggestions)}?"

        # Fuzzy search suggestions
        fuzzy_suggestions = self.trie.fuzzy_search(command, max_distance=1)
        if fuzzy_suggestions:
            return f"Did you mean: {', '.join(fuzzy_suggestions)}?"

        return "Command not recognized."
