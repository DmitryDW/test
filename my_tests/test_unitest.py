import unittest
from my_test1 import full_name

class Name_test_case(unittest.TestCase):


    def test_first_last_name(self):
        format_name = full_name('Роман', 'Кавлев')
        self.assertEqual(format_name, 'Роман Кавлев')


if __name__ == "__name__":
    unittest.main()