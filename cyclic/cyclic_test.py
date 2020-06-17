import unittest
from cyclic import solution

class CyclicTest(unittest.TestCase):
    def test_fail(self):
        A = [1,1, 2,3,5]
        k = 42
        self.assertEqual(solution(A,k), [3,5,1,1,2])

    def test_normal(self):
        A = [1,2,3,4]
        k = 4
        self.assertEqual(solution(A, k), A)

    def test_empty_list(self):
        A = []
        k = 3
        self.assertEqual(solution(A,k), A)

    def test_no_shift(self):
        A = [3,4,5]
        k = 0
        self.assertEqual(solution(A,k), A)

    def test_shift_one(self):
        A = [3,4]
        k = 1
        self.assertEqual(solution(A,k), [4,3])

    def test_shift_in_place(self):
        A = [3,4]
        k = 2
        self.assertEqual(solution(A,k), A)

    def test_shift_two(self):
        A = [1,2,3,4]
        k = 2
        self.assertEqual(solution(A,k), [3,4,1,2])

    def test_shift_three(self):
        A = [1,2,3,4]
        k = 3
        self.assertEqual(solution(A,k), [2,3,4,1])

    def test_single(self):
        A = [4]
        k = 1
        self.assertEqual(solution(A,k), A)
        
    def test_small1(self):
        A = [1,2,3,4,5,6,7]
        k = 1
        self.assertEqual(solution(A,k), [7, 1, 2,3,4,5,6])

    def test_small2(self):
        A = [-1,-2,-3,-4,-5,-6,-7]
        k = 1
        self.assertEqual(solution(A,k), [-7, -1, -2,-3,-4,-5,-6])

    def test_small_right_left(self):
        A = [-1,-2,-3,-4,-5,-6,-7]
        k = -1
        self.assertEqual(solution(A,k), [-2,-3,-4,-5,-6, -7, -1])
        k = 1
        self.assertEqual(solution(A,k), [-1, -2,-3,-4,-5,-6, -7])

    def test_medium_right_left(self):
        A = [-1,-2,-3,-4,-5,-6,-7]
        k = -3
        self.assertEqual(solution(A,k), [-4, -5, -6, -7, -1, -2,-3])
        k = 3
        self.assertEqual(solution(A,k), [-1,-2,-3,-4, -5,-6, -7])

    def test_small2(self):
        #K >= N
        k = 10
        A =  [1,2,3,4,5]
        self.assertEqual(solution(A, k), [1,2,3,4,5])

   #K and N are maximal: both in range [0..100], element in A are within [-1,000 to 1,000]
    def test_maximal(self):
        k = 100
        A = [i for i in range(1,101)]
        print(A)
        self.assertEqual(solution(A, k), A)


    def test_large_right_left(self):
        A = [-1,-2,-3,-4,-5,-6,-7]
        k = -6
        self.assertEqual(solution(A,k), [ -7, -1, -2,-3,-4, -5, -6])
        k = 6
        self.assertEqual(solution(A,k), [-1,-2,-3,-4, -5,-6,-7])


if __name__ == "__main__":
    unittest.main()
