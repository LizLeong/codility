import unittest 
from tape import solution

class TapeTest(unittest.TestCase):

    def test_basic(self):
        A = [3, 1, 2, 4, 3]
        self.assertEqual(solution(A), 1)

if __name__ == "__main__":
    unittest.main()
