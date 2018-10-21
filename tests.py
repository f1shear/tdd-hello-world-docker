

import unittest
from hello_world import hello_world, greet


class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World")

    def test_greet(self):
        self.assertEqual(greet('Ravi'), "Hello Ravi")


if __name__ == '__main__':
    unittest.main()
