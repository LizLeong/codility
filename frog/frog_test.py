import unittest
from frog import solution

class FrogJTest(unittest.TestCase):
    def test_no_hop(self):
        X,Y,D = 10, 10, 10
        self.assertEqual(solution(X,Y,D), 0)

    def test_single_hop1(self):
        X,Y,D = 10, 20, 10
        self.assertEqual(solution(X,Y,D), 1)

    def test_under_singnle_hop(self):
        X,Y,D = 10, 15, 10
        self.assertEqual(solution(X,Y,D), 1)

    def test_double_hop(self):
        X,Y,D = 10, 30, 10
        self.assertEqual(solution(X,Y,D), 2)

    def test_multiple_hop(self):
        X,Y,D = 10, 100, 10
        self.assertEqual(solution(X,Y,D), 9)

    def test_giant_hop(self):
        X,Y,D = 10, 1000000000, 10
        self.assertEqual(solution(X,Y,D), 99999999)


if __name__ == "__main__":
    unittest.main()
