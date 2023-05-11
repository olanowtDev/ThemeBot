import unittest
from BotFunctions import *


class TestFormatInput(unittest.TestCase):

    def test_lower_case(self):
        self.assertEqual(format_input('Test'), 'test')

    def test_strip(self):
        self.assertEqual(format_input(' Test '), 'test')

    def test_regex(self):
        self.assertEqual(format_input('Test   test  TeSt'), 'test test test')


class TestContainsTheme(unittest.TestCase):

    def test_in_database(self):
        self.assertTrue(contains_theme('foo', 'Resources/test-database-0.csv'))

    def test_not_in_database(self):
        self.assertFalse(contains_theme('fooo', 'Resources/test-database-0.csv'))


class TestGetAllThemes(unittest.TestCase):

    def test_in_order(self):
        self.assertListEqual(get_all_themes('Resources/test-database-0.csv'), ['foo', 'bar', 'spam', 'eggs',
                                                                               'photoshop', 'gimp'])

    def test_out_of_order(self):
        self.assertCountEqual(get_all_themes('Resources/test-database-0.csv'), ['bar', 'foo', 'eggs', 'spam',
                                                                                'gimp', 'photoshop'])


class TestGetUsedThemes(unittest.TestCase):

    def test_in_order(self):
        self.assertListEqual(get_used_themes('Resources/test-database-0.csv'), ['foo', 'spam', 'photoshop'])

    def test_out_of_order(self):
        self.assertCountEqual(get_used_themes('Resources/test-database-0.csv'), ['photoshop', 'spam', 'foo'])


class TestGetUnusedThemes(unittest.TestCase):

    def test_in_order(self):
        self.assertListEqual(get_unused_themes('Resources/test-database-0.csv'), ['bar', 'eggs', 'gimp'])

    def test_out_of_order(self):
        self.assertCountEqual(get_unused_themes('Resources/test-database-0.csv'), ['eggs', 'gimp', 'bar'])


if __name__ == '__main__':
    unittest.main()
