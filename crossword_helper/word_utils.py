#!/usr/bin/env python3

from itertools import permutations
from os.path import isfile
import re

# A collection of utils for words

class WordUtils:

    def __init__(self, dictionary_file: str = '/usr/share/dict/words'):
        self.words = set()

        self.dictionary_file: str = dictionary_file
        self.load_dictionary_file(dictionary_file)

    def load_dictionary_file(self, dictionary_file: str) -> None:
        """
        Load a dictionary file into memory. This is treated as the set of valid words.
        Each line of the file is treated as a word

        :param dictionary_file: A path to the dictionary file of interest
        :type dictionary_file: str
        """
        # Load a dictionary file
        if isfile(dictionary_file):
            with open(dictionary_file, 'r') as f:
                self.words = {x.strip().lower() for x in f}
        else:
            print(f'Could not load dictionary file {dictionary_file}. Some functions will not be available.')
            self.words = set()

    def is_dict_word(self, word: str) -> bool:
        """
        Return true iff the given word is a dictionary word

        :param word: The word to check
        :type word: str
        :return: Whether `word` is a dictionary word
        :rtype: bool
        """
        return word in self.words

    def get_anagrams_of(self, word: str, length: int = None) -> list:
        """
        Generate a list of anagrams contained in `word` of length `length`

        :param word: The word to check for anagrams
        :type word: str
        :param length: The desired length of anagram to check for, defaults to None
        :type length: int, optional
        :return: Sorted list of all anagrams in the word
        :rtype: list
        """
        # If the length is specified, use it, otherwise cap it to the length of the word
        if length:
            length = min(length, len(word))
        else:
            length = len(word)

        # Note: sorted returns a list
        return sorted({''.join(x) for x in permutations(word.lower(), length) if self.is_dict_word(''.join(x))})

    def get_substrings_of(self, word: str, length: int = None) -> list:
        """
        Generate a list of substrings of the words contained in `word`

        :param word: The word to check for substrings
        :type word: str
        :param length: The desired length of substring to check for, defaults to None
        :type length: int, optional
        :return: All substrings of `word` that are dictionary words
        :rtype: list
        """
        # If the length is specified, use it, otherwise cap it to the length of the word
        if length:
            length = min(length, len(word))
        else:
            length = len(word)

        out = set()
        for i in range(0, len(word) - length):
            substring: str = word[i:i+length]
            if self.is_dict_word(substring):
                out.insert(word)
        # Note: sorted returns a list
        return sorted(out)
