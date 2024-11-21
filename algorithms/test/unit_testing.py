import unittest
import os 
import sys

algorithm_folder_path = os.path.join(os.getcwd(), "algorithms")
sys.path.append(algorithm_folder_path)

from algorithm1 import count_characters_string
from algorithm2 import validate_email


class TestMethods(unittest.TestCase):

    def test_validate_email(self):
        # Test valid email addresses
        self.assertTrue(validate_email("abhishek@gmail.com"))
        self.assertTrue(validate_email("ust.global@ust.co.in"))
        self.assertTrue(validate_email("abhishek123@ust.org"))

        # Test invalid email addresses
        self.assertFalse(validate_email("invalid-email.com"))
        self.assertFalse(validate_email("abhishke"))

    def test_count_character_occurrences(self):
        # Test with a simple string
        input_string = "hello world"
        expected_output = {
            'h': 1, 'e': 1, 'l': 3, 'o': 2, 
            ' ': 1, 'w': 1, 'r': 1, 'd': 1
        }
        self.assertEqual(count_characters_string(input_string), expected_output)

        # Test with an empty string
        self.assertEqual(count_characters_string(""), {})

        # Test with a string with special characters
        input_string = "aabb@@cc##"
        expected_output = {
            'a': 2, 'b': 2, '@': 2, 'c': 2, '#': 2
        }
        self.assertEqual(count_characters_string(input_string), expected_output)


if __name__ == "__main__":
    unittest.main()
