#!/usr/bin/env python3

import unittest

from crossword_helper.word_utils import WordUtils

class TestWordUtils(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        word_utils = WordUtils()

        self.assertTrue(word_utils.dictionary_file)
        self.assertTrue(word_utils.words)

    def test_init_path(self):
        input_dictionary_file: str = '/usr/share/dict/words'
        word_utils = WordUtils(input_dictionary_file)

        self.assertEqual(input_dictionary_file, word_utils.dictionary_file)
        self.assertTrue(word_utils.words)

    def test_init_path_bad(self):
        input_dictionary_file: str = '/usr/share/dict/bad_file'
        word_utils = WordUtils(input_dictionary_file)

        self.assertEqual(input_dictionary_file, word_utils.dictionary_file)
        self.assertFalse(word_utils.words)


    def test_get_anagrams_of_default_length(self):
        word: str = 'silent'

        # A non-exhaustive sample of words that may be formed out of `word`
        expected_words: set = {'enlist', 'inlets', 'listen', 'silent', 'tinsel'}

        word_utils = WordUtils()
        anagrams: set = word_utils.get_anagrams_of(word)

        self.assertEqual(sorted(anagrams), anagrams)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, anagrams)

        self.assertTrue(all(len(x) == len(word) for x in anagrams))

    def test_get_anagrams_of_length_too_long(self):
        word: str = 'silent'
        word_length: int = len(word) + 5

        # A non-exhaustive sample of words that may be formed out of `word`
        expected_words: set = {'enlist', 'inlets', 'listen', 'silent', 'tinsel'}

        word_utils = WordUtils()
        anagrams: set = word_utils.get_anagrams_of(word)

        self.assertEqual(sorted(anagrams), anagrams)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, anagrams)

        self.assertTrue(all(len(x) == len(word) for x in anagrams))

    def test_get_anagrams_of_fixed_length(self):
        word: str = 'silent'
        word_length: int = 4

        # A non-exhaustive sample of words that may be formed out of `word`
        expected_words: set = {'isle', 'lens', 'lent', 'slit', 'tens', 'tile'}

        word_utils = WordUtils()
        anagrams: set = word_utils.get_anagrams_of(word, word_length)

        self.assertEqual(sorted(anagrams), anagrams)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, anagrams)

        self.assertTrue(all(len(x) == word_length for x in anagrams))

    def test_get_substrings_of(self):
        word: str = 'airspaces'
        word_length: int = 4

        expected_words: set = {'airs', 'pace', 'aces'}

        word_utils = WordUtils()
        substrings: list = word_utils.get_substrings_of(word, word_length)

        self.assertEqual(sorted(substrings), substrings)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, substrings)

        self.assertTrue(all(len(x) == word_length for x in substrings))

    def test_get_words_matching_pattern(self):
        pattern: str = 'a..y'

        expected_words: set = {'airy', 'ally', 'army', 'awry'}

        word_utils = WordUtils()
        matches: list = word_utils.get_words_matching_pattern(pattern)

        self.assertEqual(sorted(matches), matches)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, matches)

        self.assertTrue(all(len(x) == len(pattern) for x in matches))
