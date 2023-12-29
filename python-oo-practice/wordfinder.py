"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self, file_path):
        """Initialize WordFinder with a path to a file containing words."""
        self.words = self.read_words(file_path)
        self.num_of_words = len(self.words)

    def read_words(self, file_path):
        """Read words from the specified file and return a list of words."""
        try:
            with open(file_path, 'r') as file:
                return [word.strip() for word in file.readlines()]
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return []

    def random(self):
        """Return a random word from the list of words."""
        if self.num_of_words == 0:
            print("No words available.")
            return None
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    def read_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return [word.strip() for word in file.readlines() if not self.is_comment_or_blank(word)] 
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return[]
        
    def is_comment_or_blank(self, line):    
        """Check if a line is a comment or blank"""
        return line.strip() == '' or line.strip().startswith('#')

