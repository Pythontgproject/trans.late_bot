import unittest
import main

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual((main.test_test(3), main.test_test(5)), (9, 25))


if __name__ == '__main__':
    unittest.main()
