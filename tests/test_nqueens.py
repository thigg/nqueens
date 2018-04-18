import unittest

from hundredsemesterslater import *


class MyTest(unittest.TestCase):
    """
    Test the n-queens python implementation
    """

    def testInvalidParams(self):
        """
        tests invalid parameters.
        """
        with self.assertRaises(ValueError):
            nqueens(-1)
            nqueens(0)
            nqueens(1.5)
            nqueens("1")

    def testSmallN(self):
        """
        tests small arguments for quick tests.
        """
        # Solutions from wikipedia!
        for idx, solution in enumerate(
                [(1, 1), (0, 0), (0, 0), (2, 1), (10, 2), (4, 1), (40, 6), (92, 12), (352, 46), (724, 92),
                 (2680, 341)]):
            self.assertEqual(nqueens(idx + 1), solution)


    #def test13(self):
    #    self.assertEqual(nqueens(13), (73712,9233))

    def testMuts(self):
        """
        Test the mutation method
        """
        self.assertEqual(getMutations(1, (0,)), [(0,)])
        self.assertEqual(getMutations(2, (0, 1)), [(0, 1), (1, 0)])
        self.assertEqual(getMutations(3, (0, 2, 1)), [(1, 0, 2), (0, 2, 1), (1, 2, 0), (2, 0, 1)])
        self.assertEqual(getMutations(4, (1, 3, 0, 2)), [(1, 3, 0, 2), (2, 0, 3, 1)])

    def testRotation(self):
        """
        simple tests of the rotation method
        """
        self.assertEqual(rotate(3, (2, 0, 1)), (0, 2, 1))
        self.assertEqual(rotate(3, (0, 2, 1)), (1, 2, 0))
        self.assertEqual(rotate(1, (0,)), (0,))
