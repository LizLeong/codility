import unittest
from max_counter import solution

class MaxCounterTest(unittest.TestCase):
    def test_big_counter(self):
        N =100000 
        A = [1] * 100000 
        expected = [100000] * 100000 
        self.assertEqual(solution(N, A), expected)

    def test_big_array(self):
        N = 5
        A = [100000] * 5
        expected = [0] * 5
        self.assertEqual(solution(N, A), expected)

    def test_example(self):
        N = 5
        A = [3,4,4,6,1,4,4]
        expected = [3,2,2,4,2]
        self.assertEqual(solution(N, A), expected)


if __name__ == "__main__":
    unittest.main()
