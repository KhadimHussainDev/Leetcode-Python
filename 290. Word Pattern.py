class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}  # Maps each character in the pattern to a word
        word_to_pattern = {}  # Maps each word to a character in the pattern

        words = s.split()

        # Check if the pattern length is equal to the number of words
        if len(pattern) != len(words):
            return False

        for char, word in zip(pattern, words):
            if char not in pattern_to_word:
                # Check if the word is already mapped to another character
                if word in word_to_pattern:
                    return False
                pattern_to_word[char] = word
                word_to_pattern[word] = char
            else:
                if pattern_to_word[char] != word:
                    return False

        return True
