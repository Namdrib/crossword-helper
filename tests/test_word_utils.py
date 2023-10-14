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

        word_utils = WordUtils()

        anagrams: set = word_utils.get_anagrams_of(word)
        expected_words: set = {'enlist', 'inlets', 'listen', 'silent', 'tinsel'}

        self.assertEqual(sorted(anagrams), anagrams)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, anagrams)


    def test_get_anagrams_of_fixed_length(self):
        word: str = 'silent'

        word_utils = WordUtils()

        anagrams: set = word_utils.get_anagrams_of(word, 4)
        # A non-exhaustive list of words that may be formed out of `word`
        expected_words: set = {'isle', 'lens', 'lent', 'slit', 'tens', 'tile'}

        self.assertEqual(sorted(anagrams), anagrams)
        for expected_word in expected_words:
            with self.subTest(word=expected_word):
                self.assertIn(expected_word, anagrams)
