"""Test the a2ahk module"""
import uuid
import unittest
import os.path
from functools import partial

import a2ahk

TEST_CONTENT = """; some random ahk comment
a_string := "lorem ipsum... "
  anIndentedString = asvasd asdfasd asdfasd
a_bool := false
a_number = 42133723
a_float = 123.567
"""


class Test(unittest.TestCase):
    def test_get_set_vars(self):
        test_file = _get_test_ahk_path()
        with open(test_file, 'w') as fob:
            fob.write(TEST_CONTENT)

        ahkvars = a2ahk.get_variables(test_file)
        self.assertEqual(len(ahkvars), 4)
        self.assertTrue('a_string' in ahkvars)
        self.assertEqual(ahkvars['a_string'], 'lorem ipsum...')

        a2ahk.set_variable(test_file, 'a_bool', True)
        ahkvars = a2ahk.get_variables(test_file)
        self.assertTrue(ahkvars['a_bool'])
        self.assertRaises(KeyError, partial(a2ahk.set_variable, test_file, 'MissingName', False))
        a2ahk.set_variable(test_file, 'a_number', 1)
        ahkvars = a2ahk.get_variables(test_file)
        self.assertEqual(ahkvars['a_number'], 1)
        test_string = 'a rose is a rose...'
        a2ahk.set_variable(test_file, 'a_string', test_string)
        ahkvars = a2ahk.get_variables(test_file)
        self.assertEqual(ahkvars['a_string'], test_string)

        os.remove(test_file)
        self.assertFalse(os.path.isfile(test_file))

    def test_get_set_vars_new_file(self):
        test_file = _get_test_ahk_path()
        self.assertFalse(os.path.isfile(test_file))
        for key, value in (('somekey', 'Monkeys'), ('another', 4815162342)):
            a2ahk.set_variable(test_file, key, value)
            self.assertTrue(os.path.isfile(test_file))
            vars = a2ahk.get_variables(test_file)
            self.assertTrue(key in vars)
            self.assertTrue(vars[key] == value)
            os.remove(test_file)
            self.assertFalse(os.path.isfile(test_file))

    def test_create_vars(self):
        """Test adding lines to files or re-using last empty line."""
        for content in TEST_CONTENT, TEST_CONTENT.strip():
            test_file =_get_test_ahk_path()
            with open(test_file, 'w') as fob:
                fob.write(content)

            key, value = str(uuid.uuid4()), str(uuid.uuid4())
            a2ahk.set_variable(test_file, key, value, create_key=True)
            ahkvars = a2ahk.get_variables(test_file)
            self.assertEqual(ahkvars[key], value)

    def test_string_convert(self):
        result = a2ahk.convert_string_to_type('string')
        self.assertTrue(isinstance(result, str))
        self.assertEqual('string', result)
        result = a2ahk.convert_string_to_type('true')
        self.assertTrue(result)
        result = a2ahk.convert_string_to_type('faLSe')
        self.assertFalse(result)
        result = a2ahk.convert_string_to_type('345243')
        self.assertTrue(isinstance(result, int))
        result = a2ahk.convert_string_to_type('345243.')
        self.assertTrue(isinstance(result, float))

    def test_py_value_to_string(self):
        for item, result in [
            (True, 'true'),
            (False, 'false'),
            ('String', '"String"'),
            (0.333, '0.333'),
            (1337, '1337'),
            (['something', 42, 13.37], '["something", 42, 13.37]'),
        ]:
            converted = a2ahk.py_value_to_ahk_string(item)
            self.assertEqual(converted, result)

    def test_ensure_ahk_ext(self):
        base = str(uuid.uuid4())
        name = a2ahk.ensure_ahk_ext(base)
        parts = os.path.splitext(name)
        self.assertEqual(parts[0], base)
        self.assertEqual(parts[1], a2ahk.EXTENSION)

    def test_call_lib_cmd(self):
        win_startup_path = a2ahk.call_lib_cmd('get_win_startup_path')
        print('win_startup_path: "%s"' % win_startup_path)


def _get_test_ahk_path():
    return os.path.join(os.getenv('temp'), str(uuid.uuid4()) + a2ahk.EXTENSION)


if __name__ == '__main__':
    unittest.main()
