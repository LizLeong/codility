import unittest

from pme import solution

class PmeTest(unittest.TestCase):
    def test_empty(self):
        A = []
        self.assertEqual(solution(A), 1)

    def test_single_begin(self):
        A = [1]
        self.assertEqual(solution(A), 2)

    def test_single_end(self):
        A = [2]
        self.assertEqual(solution(A), 1)

    def test_sorted_begin(self):
        A = [ 2, 3, 4]
        self.assertEqual(solution(A), 1)
        
    def test_sorted_end(self):
        A = [ 1, 2, 3, 4]
        self.assertEqual(solution(A), 5)
        
    def test_sorted_middle(self):
        A = [ 1, 3, 4]
        self.assertEqual(solution(A), 2)

    def test_unsorted_begin(self):
        A = [ 5, 2, 3, 4]
        self.assertEqual(solution(A), 1)
        
    def test_unsorted_end(self):
        A = [ 5, 1, 2, 3, 4]
        self.assertEqual(solution(A), 6)
        
    def test_unsorted_middle(self):
        A = [ 5, 1, 3, 4]
        self.assertEqual(solution(A), 2)

    def test_large(self):
        A = [x for x in range(1,100001)]
        self.assertEqual(solution(A), 100001)


if __name__ == "__main__":
    unittest.main()
