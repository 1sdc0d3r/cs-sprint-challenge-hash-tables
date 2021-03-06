import unittest

from ex3 import intersection


class TestEx2(unittest.TestCase):

    def test_small(self):
        result = intersection([
            [1, 2, 3],
            [1, 4, 5],
            [1, 6, 7]
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1, 2],
            [1],
        ])
        self.assertTrue(result == [1])

        result = intersection([
            [1, 2, 3],
            [1, 4, 5, 3],
            [1, 6, 7, 3]
        ])
        result.sort()
        self.assertTrue(result == [1, 3])

    def test_large(self):
        arrays = [
            list(range(1000, 2000)) + [1, 2, 3],
            list(range(2000, 3000)) + [1, 2, 3],
            list(range(3000, 4000)) + [1, 2, 3],
            list(range(4000, 5000)) + [1, 2, 3],
            list(range(5000, 6000)) + [1, 2, 3],
            list(range(6000, 7000)) + [1, 2, 3],
            list(range(7000, 8000)) + [1, 2, 3],
            list(range(8000, 9000)) + [1, 2, 3],
            list(range(9000, 10000)) + [1, 2, 3],
            list(range(10000, 11000)) + [1, 2, 3]
        ]

        result = intersection(arrays)
        result.sort()
        self.assertTrue(result == [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
